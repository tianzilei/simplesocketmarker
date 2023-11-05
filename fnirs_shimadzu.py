def handle_client(client, servermsg):
    if servermsg == "marker":
        client.send('marker'.encode("utf-8"))
    elif servermsg == "accepted":
        pass
    else:
        print(f"Received:{servermsg}")

