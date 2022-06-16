from discord_webhooks import DiscordWebhooks

webhook_url = ''

def send_msg(ssh, vnc):

    WEBHOOK_URL = webhook_url 

    webhook = DiscordWebhooks(WEBHOOK_URL)
    webhook.set_footer(text='-- thesynthax')

    webhook.set_content(title='Raspberry Pi Online', description="Here are the port numbers.")
    webhook.add_field(name='SSH/VNC: ', value="")
    webhook.add_field(name='-> ', value=ssh + "\n" + vnc)

    webhook.send()

    print("Sent message to discord")