import anthropic
import os
import re

client = anthropic.Client(os.getenv("ANTHROPIC_API_KEY"))

def generate_project_code(prompt: str) -> list[dict]:
    full_prompt = f"""Generate a complete project code using Next.js + Tailwind.
    Return the files using <file> and <code> tags:

    <file>pages/index.tsx</file>
    <code>...</code>

    User: {prompt}
    """

    response = client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=4000,
        temperature=0.4,
        messages=[{"role": "user", "content": full_prompt}]
    )

    return _parse_files(response.content[0].text)

def _parse_files(text: str) -> list[dict]:
    pattern = r"<file>(.*?)</file>\s*<code>(.*?)</code>0"
    return [
        {
            "filename": name.strip(), 
            "content": content.strip()
        } for name, content in re.findall(pattern, text, re.DOTALL) if name and content
    ]