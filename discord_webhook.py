from discord_webhooks import DiscordWebhooks

webhook_url = 'https://discord.com/api/webhooks/986912518159106068/eklOK5k5lAZjveUS-p7Z_ciongoZd-3cDlIEhk4Vk5BJ4GGSfdwi-CRsmojewAo5sysv'

def send_msg(ssh, vnc):

    WEBHOOK_URL = webhook_url 

    message = ssh + "\n" + vnc

    webhook = DiscordWebhooks(WEBHOOK_URL)
    webhook.set_footer(text='-- thesynthax')

    webhook.set_content(title='Raspberry Pi Online', description="Here are the port numbers.")

    webhook.add_field(name='SSH/VNC: ', value=message)

    webhook.send()

    print("Sent message to discord")
