from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
ip = env.str("ip")  # Тоже str, но для айпи адреса хоста
PGUSER = env.str("PGUSER")
PGPASSWORD = env.str("PGPASSWORD")
DATABASE = env.str("DATABASE")
WALLET_LTC = env.str("WALLET_LTC")
BLOCKCYPHER_TOKEN = env.str("BLOCKCYPHER_TOKEN")
REQUEST_LINK = "bitcoin:{address}?" \
               "amount={amount}" \
               "&label={message}"

QIWI_TOKEN = env.str("qiwi")
WALLET_QIWI = env.str("wallet")
QIWI_PUBKEY = env.str("qiwi_p_pub")
POSTGRES_URL = f"postgresql://{PGUSER}:{PGPASSWORD}@{ip}/{DATABASE}"

