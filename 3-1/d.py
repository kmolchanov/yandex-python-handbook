while (log_message := input()) != '':
    if (log_message.endswith('@@@')):
        continue
    print(log_message.lstrip('##'))
