import sentry_sdk

from bot.bot import Bot


def main():
    sentry_sdk.init(
        "https://1e0df56b7d12486fb0fea9fe2a47cb0f@o472074.ingest.sentry.io/5744827",

        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        # We recommend adjusting this value in production.
        traces_sample_rate=1.0
    )

    bot = Bot()
    bot.tweet()


if __name__ == "__main__":
    main()
