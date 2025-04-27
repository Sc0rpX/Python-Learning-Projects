import random

words = [
    "python", "java", "hangman", "developer", "programmer", "keyboard", "monitor", "algorithm", "function", "variable",
    "debugging", "computer", "software", "hardware", "internet", "database", "security", "hacker", "network", "password",
    "encryption", "firewall", "malware", "cybersecurity", "processor", "compiler", "syntax", "runtime", "terminal", "command",
    "framework", "backend", "frontend", "javascript", "artificial", "intelligence", "robotics", "automation", "virtual", "cloud",
    "blockchain", "cryptography", "encoding", "decoding", "iteration", "recursion", "binary", "server", "client", "storage",
    "protocol", "cookie", "session", "gateway", "router", "switch", "packet", "payload", "trojan", "worm",
    "phishing", "spyware", "adware", "exploit", "rootkit", "forensics", "linux", "windows", "macintosh", "kernel",
    "bash", "shell", "commandline", "script", "object", "class", "inheritance", "polymorphism", "abstraction", "interface",
    "method", "attribute", "array", "list", "dictionary", "tuple", "loop", "condition", "boolean", "integer",
    "float", "string", "char", "exception", "handler", "thread", "process", "module", "library", "package"
]

def random_word():
    return random.choice(words)