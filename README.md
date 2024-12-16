# 🎄 LabyMod Advent Tracker

[![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

> Automated LabyMod advent calendar tracker with Discord notifications. Never miss a daily reward again!


## 🌟 Highlights

- 🔄 **Real-time Tracking**: Automatically monitors LabyMod's advent calendar
- 🎯 **Instant Notifications**: Sends alerts to Discord when new rewards are available
- 🔒 **Secure**: Environment-based credential management
- 📊 **Detailed Logging**: Comprehensive activity tracking
- ⚡ **Lightweight**: Minimal resource usage
- 🛠 **Configurable**: Easy to customize check intervals and notifications

## 📋 Requirements

- Python 3.7+
- Discord server with webhook permissions
- LabyMod account
- Internet connection

## 🚀 Quick Start

### 1️⃣ Installation

```bash
# Clone the repository
git clone https://github.com/9de/labymod-advent-AutoClaimer.git
cd labymod-advent-tracker

# Install dependencies
pip install -r requirements.txt
```

### 2️⃣ Configuration

Create a `.env` file:

```env
# Required credentials
DISCORD_WEBHOOK_URL="your-webhook-url"
LABY_SESSION_ID="your-session-id"
LABY_LIVE_TOKEN="your-live-token"
```

### 3️⃣ Run

```bash
python index.py
```

## 🔧 Detailed Setup

### Discord Webhook Setup

1. Open Discord Server Settings
2. Navigate to `Integrations` → `Webhooks`
3. Click `New Webhook`
4. Name your webhook and choose a channel
5. Copy the webhook URL

### LabyMod Credentials

1. Log into [LabyMod](https://labymod.net)
2. Access Developer Tools (F12)
3. Navigate to Application → Cookies
4. Find and copy:
   - `LABY_SESSION_ID`
   - `lm_long_live_token`

## 📊 Features In-Depth

### Automated Checking

```python
check_interval = 3600  # Default: 1 hour
```

The tracker automatically:
- Monitors the advent calendar based on current date
- Validates available rewards
- Sends immediate notifications
- Retries on failures

### Logging System

```plaintext
2024-12-16 10:00:00 - INFO - Starting Advent Calendar Checker
2024-12-16 10:00:01 - INFO - Successfully checked day 16
```

Logs are stored in `advent_calendar.log` with:
- Timestamp
- Log level
- Detailed event description

### Error Recovery

- Automatic retry on network failures
- Graceful handling of API errors
- Configuration validation
- Detailed error reporting

## 🔐 Security Best Practices

1. **Credential Management**
   - Never commit `.env` file
   - Rotate credentials regularly
   - Use environment-specific configurations

2. **Access Control**
   - Limit webhook permissions
   - Monitor access logs
   - Regular security audits

## 🛠 Advanced Configuration

### Custom Check Intervals

```python
checker = AdventCalendarChecker()
checker.run(check_interval=1800)  # Check every 30 minutes
```

### Logging Levels

```python
logging.basicConfig(
    level=logging.DEBUG,  # More detailed logging
    format='%(asctime)s - %(levelname)s - %(message)s'
)
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. Commit changes
   ```bash
   git commit -m 'Add amazing feature'
   ```
4. Push to branch
   ```bash
   git push origin feature/amazing-feature
   ```
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) for details.

## 🙏 Acknowledgments

- LabyMod team for the advent calendar
- Discord for webhook functionality
- Open source community for inspiration

## 📞 Support

- 📧 Create an issue for bug reports
- 💡 Feature requests are welcome
- 📚 Wiki for additional documentation

## 🗺 Roadmap

- [ ] GUI Interface
- [ ] Multiple calendar support
- [ ] Custom notification templates
- [ ] Statistics dashboard
- [ ] Mobile notifications

---

<div align="center">
Made with ❤️ by the community
</div>
