from langchain.agents import initialize_agent, Tool
from langchain_community.llms import Ollama

from tools.k8s_logs import get_pod_logs
from tools.k8s_fix import fix_pod_issue

llm = Ollama(model="llama3")

tools = [
    Tool(name="Logs", func=get_pod_logs, description="Get pod logs"),
    Tool(name="Fix", func=fix_pod_issue, description="Restart deployment")
]

agent = initialize_agent(tools, llm, agent="zero-shot-react-description")

response = agent.run("Check why pod is failing and fix it")
print(response)
