from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core.agent import Agent
from rasa_core.policies import FormPolicy
from rasa_core.policies.embedding_policy import EmbeddingPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.policies.fallback import FallbackPolicy
from policy.attention_policy import AttentionPolicy


def train_nlu_gao():
    from rasa_nlu_gao.training_data import load_data
    from rasa_nlu_gao import config
    from rasa_nlu_gao.model import Trainer

    training_data = load_data('data/training.md')
    trainer = Trainer(config.load("configs/nlu_config.yml"))
    trainer.train(training_data)
    model_directory = trainer.persist('models/nlu_gao/',
                                      fixed_model_name="current")

    return model_directory


def train_nlu():
    from rasa_nlu.training_data import load_data
    from rasa_nlu import config
    from rasa_nlu.model import Trainer

    training_data = load_data('data/nlu.md')
    trainer = Trainer(config.load("configs/nlu_embedding_config.yml"))
    trainer.train(training_data)
    model_directory = trainer.persist('models/nlu/', fixed_model_name="New")

    return model_directory


def train_dialogue_keras(domain_file="Config/_domain.yml",
                         model_path="models/new_dialogue_keras",
                         training_data_file="data/nlu.md"):
    fallback = FallbackPolicy(
        fallback_action_name="action_default_fallback",
        nlu_threshold=0.5,
        core_threshold=0.3
    )

    from policy.mobile_policy import MobilePolicy
    agent = Agent(domain_file,
                  policies=[MemoizationPolicy(max_history=5),
                            MobilePolicy(epochs=100, batch_size=16), fallback])

    training_data = agent.load_data(training_data_file)
    agent.train(
        training_data,
        validation_split=0.2
    )

    agent.persist(model_path)
    return agent


def train_dialogue_transformer(domain_file="domain.yml",
                               model_path="models/dialogue_transformer",
                               training_data_file="data/story.md"):

    fallback = FallbackPolicy(
        fallback_action_name="action_unknown_intent",
        nlu_threshold=0.7,
        core_threshold=0.3
    )

    agent = Agent(domain_file,
                  policies=[FormPolicy(),
                            AttentionPolicy(epochs=100), fallback])

    training_data = agent.load_data(training_data_file)
    agent.train(
        training_data,
        validation_split=0.2
    )

    agent.persist(model_path)
    return agent


def train_dialogue_embed(domain_file="config/_domain.yml",
                         model_path="models/new_dialogue_embed",
                         training_data_file="data/stories.md"):
    fallback = FallbackPolicy(
        fallback_action_name="action_default_fallback",
        nlu_threshold=0.5,
        core_threshold=0.3
    )

    agent = Agent(domain_file,
                  policies=[MemoizationPolicy(max_history=5),
                            EmbeddingPolicy(epochs=100), fallback])

    training_data = agent.load_data(training_data_file)
    agent.train(
        training_data,
        validation_split=0.2
    )

    agent.persist(model_path)
    return agent

# train_dialogue_keras()
# train_nlu()
train_dialogue_embed()

# python -m rasa_core_sdk.endpoint --actions actions &

# python -m rasa_core.run -d models/dialogue_keras
#  --endpoints endpoints.yml

# python -m rasa_core.train interactive -o models/dialogue -d config/_domain.yml -c policy/keras_policy.yml -s data/story.md --nlu models/nlu/default/current --endpoints endpoints.yml
# python -m rasa_core.train interactive -o models/new_dialogue_embed -d config/_domain.yml -c policy/embed_policy.yml -s data/stories.md --nlu models/nlu/default/new --endpoints endpoints.yml

