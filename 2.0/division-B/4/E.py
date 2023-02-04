def main():
    n = int(input())
    topics = {}
    messages = []
    mx = 0
    mx_topic = None
    for i in range(n):
        k = int(input())
        if k == 0:
            topic = input()
            _ = input()
            messages.append(topic)
            topics[topic] = 1
        else:
            _ = input()
            topic = messages[k - 1]
            topics[topic] += 1
            messages.append(topic)
        if topics[topic] > mx:
            mx = topics[topic]
            mx_topic = topic
    if mx_topic:
        print(mx_topic)


if __name__ == "__main__":
    main()
