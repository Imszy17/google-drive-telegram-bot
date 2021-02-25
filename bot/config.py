class config:
    BOT_TOKEN = ""
    APP_ID = ""
    API_HASH = ""
    DATABASE_URL = ""
    SUDO_USERS = "" # Sepearted by space.
    SUPPORT_CHAT_LINK = ""
    DOWNLOAD_DIRECTORY = "./downloads/"
    G_DRIVE_CLIENT_ID = ""
    G_DRIVE_CLIENT_SECRET = ""


class BotCommands:
  Download = ['download', 'dl']
  Authorize = ['auth', 'authorize']
  SetFolder = ['setfolder', 'setfl']
  Revoke = ['revoke']
  Clone = ['copy', 'clone']
  Delete = ['delete', 'del']
  EmptyTrash = ['emptyTrash']
  YtDl = ['ytdl']

class Messages:
    START_MSG = "**Halo {}.**\n__Saya Bot Pengunggah Google Drive. Anda dapat menggunakan saya untuk mengunggah file / video apa pun ke Google Drive dari tautan langsung atau dari file Telegram.__\n__dapatkan bantuan dengan klik /help.__"

    HELP_MSG = [
        ".",
        "**Google Drive Uploader**\nSaya dapat mengunggah file dari tautan langsung atau File Telegram ke Google Drive Anda. Yang saya butuhkan hanyalah mengautentikasi saya ke Akun Google Drive Anda dan mengirim tautan unduhan langsung atau File Telegram.",
        
        f"**Authenticating Google Drive**\nKirim perintah /{BotCommands.Authorize[0]} dan Anda akan menerima URL, kunjungi URL dan ikuti langkah-langkahnya dan kirim kode yang diterima di sini, gunakan perintah /{BotCommands.Revoke[0]} untuk logout akun anda.\n\n**Catatan: Saya tidak akan mendengarkan perintah atau pesan apa pun (Kecuali perintah /{BotCommands.Authorize[0]} ) wajib login !**",
        
        f"**Direct Links**\n__Kirim direct link di chat ini dan saya akan mengunduhnya ke server, lalu mengunggahnya ke akun google drive anda. Anda dapat mengganti nama file sebelum mengunggah ke akun gdrive. kirim saja link dan nama baru yang dipisahkan dengan tanda '|'.__\n\n**__Contoh:__**\n```https://contoh.com/AFileWithDirectDownloadLink.mkv | NamaBaru.mkv```\n\n**File Telegram**\n__Untuk Mengunggah file telegram di Akun Google Drive Anda, kirimkan saja file tersebut kepada saya dan saya akan mengunduh dan mengunggahnya ke Akun Google Drive Anda. Catatan: Pengunduhan File Telegram lambat. mungkin perlu waktu lebih lama untuk file besar.__\n\n**Dukungan YouTube-DL**\n__Unduh file melalui youtube-dl.\nGunakan /{BotCommands.YtDl[0]} (YouTube Link/YouTube-DL Supported site link)__",
        
        f"**Custom Folder for Upload**\n__Agar file gdrive anda lebih rapi, buatlah folder di gdrive anda dan__\nGunakan /{BotCommands.SetFolder[0]} (Link folder) untuk menerapkan folder.\nSemua file akan diupload ke folder tersebut.__\n\n**Catatan:**\ndisarankan agar folder anda dapat diakses siapa saja, dengan mengubah privasi folder",
        
        f"**Delete Google Drive Files**\n__Untuk menghapus file yang telah diupload. gunakan /{BotCommands.Delete[0]} (link File) atau balaskan perintah /{BotCommands.Delete[0]} ke link upload yang dikirim bot.\nAnda juga dapat menghapus file sampah dengan perintah /{BotCommands.EmptyTrash[0]}\nNote: file akan dihapus permanen. Proses ini tidak dapat dibatalkan\n\n**Salin file dari link gdrive**\n__Untuk menyalin file dari link gdrive\ngunakan perintah /{BotCommands.Clone[0]} (File id / Folder id atau link gdrive).__",
        
        "**Rules & Precautions**\n1. Jangan salin/unggah file besar, kemungkinan bot akan hang atau rusak\n2. Jangan spam ke bot\n3. Jangan kirim link lambat\n4. Jangan menyalahgunakan layanan gratis ini.",
        
        # Dont remove this ↓ if you respect developer.
        "**Managed by @Imszy01\nBig thanks to @viperadnan for source**"
        ]
     
    RATE_LIMIT_EXCEEDED_MESSAGE = "❗ **Rate Limit Exceeded.**\n__User rate limit exceeded try after 24 hours.__"
    
    FILE_NOT_FOUND_MESSAGE = "❗ **File/Folder not found.**\n__File id - {} Not found. Make sure it\'s exists and accessible by the logged account.__"
    
    INVALID_GDRIVE_URL = "❗ **Invalid Google Drive URL**\nMake sure the Google Drive URL is in valid format."
    
    COPIED_SUCCESSFULLY = "✅ **Copied successfully.**\n[{}]({}) __({})__"
    
    NOT_AUTH = f"🔑 **You have not authenticated me to upload to any account.**\n__Send /{BotCommands.Authorize[0]} to authenticate.__"
    
    DOWNLOADED_SUCCESSFULLY = "📤 **Mengunggah file ke gdrive...**\n**Nama file:** ```{}```\n**ukuran:** ```{}```"
    
    UPLOADED_SUCCESSFULLY = "✅ **File telah diunggah.**\n[{}]({}) __({})__"
    
    DOWNLOAD_ERROR = "❗**Unduhan gagal**\n{}\n__Link - {}__"
    
    DOWNLOADING = "📥 **Mengunduh file ke server...\nLink:** ```{}```"
    
    ALREADY_AUTH = "🔒 **Bot telah tertaut pada akun google drive anda.**\n__gunakan /revoke untuk mengeluarkan akun.__\n__Kirim saya tautan langsung atau file untuk diunggah ke gdrive__"
    
    FLOW_IS_NONE = f"❗ **Invalid Code**\n__Run {BotCommands.Authorize[0]} first.__"
    
    AUTH_SUCCESSFULLY = '🔐 **Authorized Google Drive account Successfully.**'
    
    INVALID_AUTH_CODE = '❗ **Invalid Code**\n__The code you have sent is invalid or already used before. Generate new one by the Authorization URL__'
    
    AUTH_TEXT = "🤖 **Anda perlu masuk ke akun google drive terlebih dahulu melalui [URL]({}) ini, salin kode yang tertampil, lalu kirimkan ke bot ini.**\n__Kunjungi URL > Izinkan > anda akan melihat kode > salin > kirim ke bot ini__"
    
    DOWNLOAD_TG_FILE = "📥 **Mengunduh file ke server...**\n**Nama file:** ```{}```\n**ukuran:** ```{}```\n**Tipe file:** ```{}```"
    
    PARENT_SET_SUCCESS = '🆔✅ **Custom Folder link set successfully.**\n__Your custom folder id - {}\nUse__ ```/{} clear``` __to clear it.__'
    
    PARENT_CLEAR_SUCCESS = f'🆔🚮 **Custom Folder ID Cleared Successfuly.**\n__Use__ ```/{BotCommands.SetFolder[0]} (Folder Link)``` __to set it back__.'
    
    CURRENT_PARENT = "🆔 **Your Current Custom Folder ID - {}**\n__Use__ ```/{} (Folder link)``` __to change it.__"
    
    REVOKED = f"🔓 **Revoked current logged account successfully.**\n__Use /{BotCommands.Authorize[0]} to authenticate again and use this bot.__"
    
    NOT_FOLDER_LINK = "❗ **Invalid folder link.**\n__The link you send its not belong to a folder.__"
    
    CLONING = "🗂️ **Menyalin ke google drive...**\n__Tautan GDrive - {}__"
    
    PROVIDE_GDRIVE_URL = "**❗ Provide a valid Google Drive URL along with commmand.**\n__Usage - /{} (GDrive Link)__"
    
    INSUFFICIENT_PERMISSONS = "❗ **You have insufficient permissions for this file.**\n__File id - {}__"
    
    DELETED_SUCCESSFULLY = "🗑️✅ **File berhasil dihapus.**\n__File dihapus secara permanen !\nFile id - {}__"
    
    WENT_WRONG = "⁉️ **ERROR: SOMETHING WENT WRONG**\n__Please try again later.__"
    
    EMPTY_TRASH = "🗑️🚮**Sampah berhasil dihapus !**"
    
    PROVIDE_YTDL_LINK = "❗**Provide a valid YouTube-DL supported link.**"
