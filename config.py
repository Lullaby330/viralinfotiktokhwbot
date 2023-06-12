import os

import logging

from logging.handlers import RotatingFileHandler

#Bot token @Botfather

TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5853200599:AAFpcGrjPn3t5x1yC3Ceag3_yCWpF8xsGJY")

#Your API ID from my.telegram.org

APP_ID = int(os.environ.get("APP_ID", "6216349"))

#Your API Hash from my.telegram.org

API_HASH = os.environ.get("API_HASH", "5c7418e9f3df6db931caa7354521c55f")

#Your db channel Id

CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001734154791"))

#OWNER ID

OWNER_ID = int(os.environ.get("OWNER_ID", "1289438071"))

#Database 

DB_URI = os.environ.get("DATABASE_URL", "postgres://plmvkijfoorbky:26143878d801bb396773296fed5e9b242b1b354750db1d1fd8c0c64affb8ee30@ec2-44-198-82-71.compute-1.amazonaws.com:5432/dcpobo1p96etd8")

#force sub channel id, if you want enable force sub

FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001739942775"))

FORCE_SUB_GROUP = int(os.environ.get("FORCE_SUB_GROUP", "-1001570556056"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message

START_MSG = os.environ.get("START_MESSAGE", "Hai {first} Kamu Harus Join Channel Dan Grup Terlebih Dahulu Sebelum Bisa Melihat Link Video ini.\n\nTutorial :\n|-[1.  Klik Start/Mulai\n|-[2. Wajib Join Channel :\n       * https://t.me/+yxKqV1nBGB4xZTY9\n       * https://t.me/+nns6ZvyI66Y0NWY1\n|-[3. Klik Try Again dan Start\n|-[4. Tunggu Hingga Video Muncul\n|-[5. Selamat Menikmati Asupan nya\n\nNote :\nJangan spam ya karna bisa membuat bot delayed.")

try:

    ADMINS=[]

    for x in (os.environ.get("ADMINS", "1289438071 5084234580 5220678179").split()):

        ADMINS.append(int(x))

except ValueError:

        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 

FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hai {first} Kamu Harus Join Channel Dan Grup Terlebih Dahulu Sebelum Bisa Melihat Link Video ini.\n\nTutorial :\n|-[1.  Klik Start/Mulai\n|-[2. Wajib Join Channel :\n       * https://t.me/+yxKqV1nBGB4xZTY9\n       * https://t.me/+nns6ZvyI66Y0NWY1\n|-[3. Klik Try Again dan Start\n|-[4. Tunggu Hingga Video Muncul\n|-[5. Selamat Menikmati Asupan nya\n\nNote :\nJangan spam ya karna bisa membuat bot delayed.")

#set your Custom Caption here, Keep None for Disable Custom Caption

CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button

if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True':

    DISABLE_CHANNEL_BUTTON = True

else:

    DISABLE_CHANNEL_BUTTON = False

ADMINS.append(OWNER_ID)

ADMINS.append(5220678179)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(

    level=logging.INFO,

    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",

    datefmt='%d-%b-%y %H:%M:%S',

    handlers=[

        RotatingFileHandler(

            LOG_FILE_NAME,

            maxBytes=50000000,

            backupCount=10

        ),

        logging.StreamHandler()

    ]

)

logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:

    return logging.getLogger(name)import os

import logging

from logging.handlers import RotatingFileHandler

#Bot token @Botfather

TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5853200599:AAFpcGrjPn3t5x1yC3Ceag3_yCWpF8xsGJY")

#Your API ID from my.telegram.org

APP_ID = int(os.environ.get("APP_ID", "6216349"))

#Your API Hash from my.telegram.org

API_HASH = os.environ.get("API_HASH", "5c7418e9f3df6db931caa7354521c55f")

#Your db channel Id

CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001734154791"))

#OWNER ID

OWNER_ID = int(os.environ.get("OWNER_ID", "1289438071"))

#Database 

DB_URI = os.environ.get("DATABASE_URL", "postgres://plmvkijfoorbky:26143878d801bb396773296fed5e9b242b1b354750db1d1fd8c0c64affb8ee30@ec2-44-198-82-71.compute-1.amazonaws.com:5432/dcpobo1p96etd8")

#force sub channel id, if you want enable force sub

FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001739942775"))

FORCE_SUB_GROUP = int(os.environ.get("FORCE_SUB_GROUP", "-1001570556056"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message

START_MSG = os.environ.get("START_MESSAGE", "Hai {first} Kamu Harus Join Channel Dan Grup Terlebih Dahulu Sebelum Bisa Melihat Link Video ini.\n\nTutorial :\n|-[1.  Klik Start/Mulai\n|-[2. Wajib Join Channel :\n       * https://t.me/+yxKqV1nBGB4xZTY9\n       * https://t.me/+nns6ZvyI66Y0NWY1\n|-[3. Klik Try Again dan Start\n|-[4. Tunggu Hingga Video Muncul\n|-[5. Selamat Menikmati Asupan nya\n\nNote :\nJangan spam ya karna bisa membuat bot delayed.")

try:

    ADMINS=[]

    for x in (os.environ.get("ADMINS", "1289438071 5084234580 5220678179").split()):

        ADMINS.append(int(x))

except ValueError:

        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 

FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hai {first} Kamu Harus Join Channel Dan Grup Terlebih Dahulu Sebelum Bisa Melihat Link Video ini.\n\nTutorial :\n|-[1.  Klik Start/Mulai\n|-[2. Wajib Join Channel :\n       * https://t.me/+yxKqV1nBGB4xZTY9\n       * https://t.me/+nns6ZvyI66Y0NWY1\n|-[3. Klik Try Again dan Start\n|-[4. Tunggu Hingga Video Muncul\n|-[5. Selamat Menikmati Asupan nya\n\nNote :\nJangan spam ya karna bisa membuat bot delayed.")

#set your Custom Caption here, Keep None for Disable Custom Caption

CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button

if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True':

    DISABLE_CHANNEL_BUTTON = True

else:

    DISABLE_CHANNEL_BUTTON = False

ADMINS.append(OWNER_ID)

ADMINS.append(5220678179)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(

    level=logging.INFO,

    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",

    datefmt='%d-%b-%y %H:%M:%S',

    handlers=[

        RotatingFileHandler(

            LOG_FILE_NAME,

            maxBytes=50000000,

            backupCount=10

        ),

        logging.StreamHandler()

    ]

)

logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:

    return logging.getLogger(name)
