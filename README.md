# Infraware CLI 🚀

**Your AI-powered multi-cloud operations assistant for seamless cloud infrastructure management.**

Infraware CLI is an intelligent command-line interface that combines the power of AI with multi-cloud expertise to help you manage, deploy, and optimize your cloud infrastructure across Google Cloud Platform (GCP), Amazon Web Services (AWS), Microsoft Azure, and Docker environments.

## ✨ Features

### 🌐 Multi-Cloud Support
- **Google Cloud Platform (GCP)** - Complete project and resource management
- **Amazon Web Services (AWS)** - EC2, Lambda, billing, and more
- **Microsoft Azure** - Resource groups, deployments, and services
- **Docker** - Container management and orchestration

### 🤖 AI-Powered Operations
- Intelligent command interpretation and execution
- Natural language cloud operations
- Best practices recommendations
- Cost optimization suggestions
- Automated troubleshooting assistance

### 💻 Terminal Experience
- **Command Completion** - Standard bash autocompletion
- **Command History** - Persistent history with reverse search (Ctrl+R)
- **Shell Integration** - Execute shell commands alongside AI operations
- **Interactive Prompts** - Rich, colorful terminal interface

### 🧠 Contextual Memory
- **Environment Awareness** - Remembers your cloud configurations and preferences
- **Infrastructure Intelligence** - Learns your deployment patterns and resource usage
- **Adaptive Reliability** - Improves accuracy and suggestions over time
- **Context Retention** - Maintains awareness of your current project state and history
- **Personalized Workflows** - Tailors recommendations based on your usage patterns


## 📦 Installation

### Prerequisites

Before installing the Infraware CLI, ensure you have `pipx` installed on your system:

```bash
# Install pipx if you haven't already
pip install pipx

# Ensure pipx is in your PATH
pipx ensurepath
```

> **Note for Windows users** : This CLI has been tested on Linux systems. For Windows installation, please use Windows Subsystem for Linux (WSL).


### Install Infraware CLI

```bash
pipx install git+https://github.com/Infraware-dev/CLI.git
```

### Verify Installation

After installation, verify that the CLI is working correctly:

```bash
ifw
```

### Troubleshooting

If you encounter issues during installation:

- **Path issues**: Restart your terminal or run `source ~/.bashrc` (or equivalent for your shell) after running `pipx ensurepath`
- **Permission errors**: Ensure you have the necessary permissions to install packages

## 🔑 API Key Setup

To use Infraware CLI, you'll need an **Anthropic API key**. You can get one from the [Anthropic Console](https://console.anthropic.com/).

**Note:** Additional AI providers are coming soon! Stay tuned for more options.

## 🚀 Quick Start

Once installed, launch the Infraware CLI:

```bash
ifw
```

You'll be greeted with an interactive terminal where you can:

### Natural Language Commands
```bash
|>| user@hostname List all my GCP projects
|>| user@hostname Show me AWS EC2 instances in us-east-1
|>| user@hostname Check my cloud costs for this month
|>| user@hostname Create a new Docker container for my web app
```

### Direct Shell Commands
```bash
|>| user@hostname ls -la
|>| user@hostname cd /path/to/project
|>| user@hostname kubectl get pods
```

### Control Commands
- `exit` - Exit the CLI

## 💡 Example Use Cases

### Cloud Resource Management
```bash
# List all resources across clouds
Show me all my running instances across AWS and GCP

# Create infrastructure
Create a new VPC in AWS us-west-2 with public and private subnets

# Monitor costs
Compare my monthly spending between GCP and Azure
```

### Container Operations
```bash
# Docker management
List all running Docker containers and their resource usage

# Kubernetes operations
Deploy my web application to the production Kubernetes cluster

# Container optimization
Help me optimize my Docker images for better performance
```

### Troubleshooting & Monitoring
```bash
# Diagnose issues
My Lambda function is timing out, help me troubleshoot

# Set up monitoring
Create CloudWatch alarms for my EC2 instances

# Security audit
Review IAM permissions for my GCP service accounts
```

## ⌨️ Keyboard Shortcuts

- **Ctrl+R** - Reverse search through command history
- **Ctrl+L** - Clear the terminal screen
- **Ctrl+C** - Interrupt current operation
- **Ctrl+D** - Exit the CLI
- **Tab** - Smart command completion

## 🔧 Configuration

Infraware CLI automatically detects and uses your existing cloud credentials:

- **AWS** - Uses AWS CLI credentials 
- **GCP** - Uses gcloud CLI authentication
- **Azure** - Uses Azure CLI authentication
- **Docker** - Uses local Docker daemon

Make sure you're authenticated with your respective cloud providers before using Infraware CLI.

## 🎯 Command Examples

### Infrastructure Operations
```bash
# AWS Operations
Create an EC2 instance with Ubuntu 22.04 in us-east-1
List all my S3 buckets and their sizes
Set up Auto Scaling for my web servers

# GCP Operations
Show me all Compute Engine instances across all regions
Create a new Cloud Storage bucket with lifecycle policies
Deploy a Cloud Function for image processing

# Azure Operations
List all resource groups and their costs
Create a new App Service for my web application
Set up Azure Monitor for my virtual machines
```

### Cost Management
```bash
# Cost analysis
Show me my top 5 most expensive services this month
Compare costs between regions for my workloads
Suggest ways to reduce my cloud spending

# Billing alerts
Set up billing alerts for when I exceed $500/month
Show me cost trends for the last 6 months
```
# Supported MCP Tools

## Legend
- ✅ **Supported** - Ready to use
- 🚧 **In Progress** - Currently being developed

| Category | Tool | Status |
|----------|------|--------|
| **Cloud Providers** | AWS | ✅ Supported |
|  | GCP | ✅ Supported |
|  | Azure | ✅ Supported |
|  | Hetzner | 🚧 In Progress |
|  | Linode | 🚧 In Progress |
|  | DigitalOcean | 🚧 In Progress |
| **Containers** | Docker | ✅ Supported |
|  | Podman | 🚧 In Progress |
|  | Kubernetes | 🚧 In Progress |
| **Utils** | GitHub | 🚧 In Progress |

---

If you want to integrate a new MCP feel free to do it and contribute it otherwise just open an issue with your feature request and we'll work on it!

## 🤝 Contributing

We welcome contributions from the community! Our detailed contributing guidelines are currently being finalized and will be available soon at [CONTRIBUTING.md](CONTRIBUTING.md).

In the meantime, feel free to:
- Open issues to report bugs or suggest features
- Submit pull requests with clear descriptions of your changes
- Join discussions in existing issues

For questions about contributing, please open an issue and we'll be happy to help guide you.

## 📄 License

This project is licensed under the Apache-2.0 License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support (WIP)

- **Documentation**: [docs.infraware.dev](https://docs.infraware.dev)
- **Issues**: [GitHub Issues](https://github.com/Infraware-dev/CLI/issues)
- **Community**: [Join our Discord](https://discord.gg/JneH864t)

## ⚠️ Disclaimer

**Infraware CLI is currently in Alpha** and should be considered experimental software. While we're working hard to make it stable and reliable, you may encounter:

- **Unexpected behavior** or crashes during operation
- **Breaking changes** between versions without notice
- **Limited error handling** in some scenarios
- **Performance issues** or slower response times

### 🐛 Debugging and Support

If you encounter issues while using Infraware CLI:

1. **Enable verbose logging** to get detailed information:
   ```bash
   ifw -v
   ```

2. **Check the log files** for detailed error information:
   - **Location**: `~/.ifw/logs/`
   - **Format**: `log_YYYYMMDD_HHMMSS.txt` (timestamped for each session)
   - **Contains**: Full debug output, error traces, and system information

3. **Get help from the community**:
   - **Report bugs**: [Open a GitHub Issue](https://github.com/Infraware-dev/CLI/issues) with your log files attached
   - **Real-time support**: [Join our Discord](https://discord.gg/JneH864t) for immediate assistance
   - **Include details**: OS, Python version, and relevant log snippets when reporting issues

**We appreciate your patience and feedback as we work toward a stable release!**

## 🚀 What's Next?

(WIP)

---

**Made with ❤️ by the Infraware team**

*Simplifying cloud operations, one command at a time.*
