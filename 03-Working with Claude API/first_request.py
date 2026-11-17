from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic()

MODEL = "claude-sonnet-5-5"

response = client.messages.create(
    model=MODEL,
    max_tokens=300,
    output_config={"effort": "low"},
    messages=[{
        "role": "user",
        "content": "A customer asks: can I return a jacket after 20 days?"
        "Our policy allows return in 30 days."
        "Answer the customer in two sentences.",
    }],
)

print(response.model_dump_json(indent=2, exclude_none=True))
