import pytest
from src.quantum_federated_learning import quantum_seed, federated_learning_setup, train_federated_model

def test_federated_learning():
    client, data = federated_learning_setup([1.0])
    model = train_federated_model(client, data)
    assert model.weight.data.item() is not None
