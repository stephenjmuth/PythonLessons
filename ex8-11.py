
i=0
messages=['message one','message two','message three','message four','message five',]
messages_sent=[]

def send_messages(list_var):
    while list_var:
        sending=list_var.pop()
        print(f"\tSending {sending}.")
        messages_sent.append(sending)
    return messages_sent

messages_sented=send_messages(messages[:])
print(f"\nPrinting messages: {messages}")
print(f"\nPrinting sent messages: {messages_sented}")
