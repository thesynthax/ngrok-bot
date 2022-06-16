from discord_webhooks import DiscordWebhooks

webhook_url = ''

def send_msg(sshport, vncport, status):

    WEBHOOK_URL = webhook_url 

    webhook = DiscordWebhooks(WEBHOOK_URL)
    webhook.set_footer(text='-- thesynthax')

    if (status=="online"):
        webhook.set_content(title='Raspberry Pi Online', description="Here are the port numbers.")
        webhook.add_field(name='SSH Port: ', value=sshport)
        webhook.add_field(name='VNC Port', value=vncport)

    webhook.send()

    print("Sent message to discord")