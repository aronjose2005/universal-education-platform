import torch

# Bio-inspired adaptation (simplified)
def adapt_content(content, learning_style):
    adaptation_layer = torch.nn.Linear(1, 1)
    style_factor = torch.tensor([1.0 if learning_style == "visual" else 0.5])
    adapted_content = adaptation_layer(style_factor).item()
    return f"{content} adapted for {learning_style} learning (factor: {adapted_content:.2f})"
