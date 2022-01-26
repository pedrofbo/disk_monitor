import argparse
import json
import shutil

import boto3


def notify_disk_usage(threshold: float, sns_topic: str, instance_name: str):
    disk = shutil.disk_usage("/")
    if disk.used / disk.total > threshold:
        message = (
            f"Disk usage of instance {instance_name} has exceeded the "
            f"threshold of {threshold * 100}%\n"
            f"Total disk space = {disk.total / 10**9:.2f} GB\n"
            f"Used disk space = {disk.used / 10**9:.2f} GB\n"
            f"Disk usage = {disk.used / disk.total * 100:.2f}%"
        )

        sns = boto3.client("sns")
        sns.publish(
            TopicArn=sns_topic,
            Message=message,
            Subject="Disk Usage Notification"
        )
        print(message)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Check whether the disk usage is above a set threshold"
    )
    parser.add_argument(
        "-s", "--sns-topic", type=str,
        help=("SNS topic where the notification will be sent to.")
    )
    parser.add_argument(
        "-i", "--instance-name", type=str,
        help=("Name of the EC2 instance being monitored.")
    )
    parser.add_argument(
        "-t", "--threshold", type=float,
        help=("Threshold of disk usage to determine when a notification "
              "will be sent."),
        required=False, default=0.9
    )
    args = parser.parse_args()

    notify_disk_usage(
        threshold=args.threshold,
        sns_topic=args.sns_topic,
        instance_name=args.instance_name
    )
