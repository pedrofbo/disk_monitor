while [[ $# -gt 0 ]]; do
  case $1 in
    -s|--sns-topic)
      SNS_TOPIC="$2"
      shift # past argument
      shift # past value
      ;;
    -i|--instance-name)
      INSTANCE_NAME="$2"
      shift # past argument
      shift # past value
      ;;
  esac
done

echo "SNS TOPIC = ${SNS_TOPIC}"
echo "INSTANCE NAME = ${INSTANCE_NAME}"