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
    
    INVALID_GDRIVE_URL = "❗ **Tautan google drive tidak valid**\nPastikan tautan Google Drive dalam format yang valid."
    
    COPIED_SUCCESSFULLY = "✅ **Berhasil menyalin.**\n[{}]({}) ```({})```"
    
    NOT_AUTH = f"🔑 **Anda belum mengautentikasi saya untuk mengunggah ke akun mana pun.**\n__Gunakan perintah /{BotCommands.Authorize[0]} untuk autentikasi.__"
    
    DOWNLOADED_SUCCESSFULLY = "📤 **Mengunggah file ke gdrive...**\n\n**Nama file:** ```{}```\n**Ukuran:** ```{}```\n**Uploader:** @GMuploaderbot"
    
    UPLOADED_SUCCESSFULLY = "✅ **File telah diunggah.\n**Pengunggah:** @GMuploaderbot**\n**Tautan:** [{}]({})```({})```"
    
    DOWNLOAD_ERROR = "❗**Unduhan gagal**\n\n{}\n__Link: {}__"
    
    DOWNLOADING = "📥 **Mengunduh file ke server...\n\nTautan:** ```{}```\n**Uploader:** @GMuploaderbot"
    
    ALREADY_AUTH = "🔒 **Bot telah tertaut pada akun google drive anda.**\n__gunakan /revoke untuk mengeluarkan akun.__\n__Kirim saya tautan langsung atau file untuk diunggah ke gdrive__"
    
    FLOW_IS_NONE = f"❗ **Kode tidak valid**\n__Gunakan perintah {BotCommands.Authorize[0]} terlebih dahulu.__"
    
    AUTH_SUCCESSFULLY = '🔐 **Autentikasi akun berhasil!.**'
    
    INVALID_AUTH_CODE = '❗ **Kode tidak valid!**\n__Silahkan anda mengambil kode autentikasi baru__'
    
    AUTH_TEXT = "🤖 **Anda perlu masuk ke akun google drive terlebih dahulu melalui [URL]({}) ini, salin kode yang tertampil, lalu kirimkan ke bot ini.**\n__Kunjungi URL > Izinkan > anda akan melihat kode > salin > kirim ke bot ini__"
    
    DOWNLOAD_TG_FILE = "📥 **Mengunduh file ke server...**\n\n**Nama file:** ```{}```\n**Ukuran:** ```{}```\n**Tipe file:** ```{}```\n**Uploader:** @GMuploaderbot"
    
    PARENT_SET_SUCCESS = '🆔✅ **Tautan folder kustom berhasil disetel.**\n**ID folder kamu:** ```{}```\ngunakan__ ```/{} clear``` __untuk melepas folder.__'
    
    PARENT_CLEAR_SUCCESS = f'🆔🚮 **Folder kustom berhasil dilepas.**\n__gunakan__ ```/{BotCommands.SetFolder[0]} (Folder Link)``` __untuk menyetel kembali__.'
    
    CURRENT_PARENT = "🆔 **ID Folder Kustom Anda Saat Ini:** ```{}```\n__Gunakan__ ```/{} (Folder link)``` __untuk mengubahnya.__"
    
    REVOKED = f"🔓 **Anda berhasil mengeluarkan akun dari bot.**\n__Gunakan /{BotCommands.Authorize[0]} Untuk mengautentikasi kembali.__"
    
    NOT_FOLDER_LINK = "❗ **Tautan folder tidak valid.**\n__Tautan yang anda kirim tidak menunjukan folder apapun.__"
    
    CLONING = "🗂️ **Menyalin ke google drive...**\n__Tautan GDrive - {}__"
    
    PROVIDE_GDRIVE_URL = "**❗ Berikan tautan Google Drive yang valid bersama dengan perintah**\n__Contoh - /{} (GDrive Link)__"
    
    INSUFFICIENT_PERMISSONS = "❗ **Anda tidak memiliki izin untuk mengakses file ini**\n**File id:** ```{}```"
    
    DELETED_SUCCESSFULLY = "🗑️✅ **File berhasil dihapus.**\n**File dihapus secara permanen !**\n\n**ID file:** ```{}```"
    
    WENT_WRONG = "⁉️ **ERROR: ADA YANG SALAH**\n__SilahkanCoba lagi nanti.__"
    
    EMPTY_TRASH = "🗑️🚮**Sampah berhasil dihapus !**"
    
    PROVIDE_YTDL_LINK = "❗**Berikan tautan valid yang didukung YouTube-DL**"
