import xbmc, xbmcaddon, xbmcgui, xbmcplugin,os,sys
import urllib, urllib2, re, glob
import base64
import shutil
import extras
import extract
import communitybuilds
import cache
import time
import downloader
import zipfile
import ntpath
#import speedtest
#import news
#import addonfix
#import settings
#import CheckPath
#import plugintools


#My variables paths
from addon.common.addon import Addon
from addon.common.net import Net
#from metahandler import metahandlers
#metainfo=metahandlers.MetaData()

xbmc_version   =  xbmc.getInfoLabel("System.BuildVersion"); version=xbmc_version[:4]; print version
AddonTitle     =  "Kodi "+version+" Maintenance"
AddonID        =  base64.b64decode(b'QW5keS5wbHVnaW4ucHJvZ3JhbS5NYWludGVuYW5jZQ==')
ADDON          =  xbmcaddon.Addon(id=AddonID)
usrdata        =  xbmc.translatePath('special://home/userdata/addon_data/Andy.plugin.program.Maintenance/')
ARTPATH        =  'special://home/addons/'+AddonID+'/art/' + os.sep
packages       =  xbmc.translatePath(os.path.join('special://home/addons','packages'))
#
mainurl                ='https://raw.githubusercontent.com/halikus/_AndyRepo/master/'
mainurl_zips           ='https://raw.githubusercontent.com/halikus/_zip/master/'
mainurl_txt            =mainurl+'_txt/'
url_Addon_Data         =mainurl_zips+'Addon_Data.zip'
url_Addon_Data_windows =mainurl_zips+'Addon_Data_Windows.zip'
url_Addon_Data_android =mainurl_zips+'Addon_Data_Android.zip'
url_Repos              =mainurl_zips+'Addons_Repos.zip'
url_Addons             =mainurl_zips+'Addons.zip'
url_Addons_windows     =mainurl_zips+'Addons_Windows.zip'
url_Addons_android     =mainurl_zips+'Addons_Android.zip'
url_Addons_Video       =mainurl_zips+'Addons_Video.zip'
url_Addons_Video_IPTV  =mainurl_zips+'Addons_Video_IPTV.zip'
shortcutstxt           =mainurl + '_txt/shortcuts.txt'
dropboxtxt             =mainurl + '_txt/dropbox.txt'
librtmp                =mainurl + '_txt/librtmp.dll'
TvPy                   =mainurl + '_txt/Clear_Cache.py'
#
url_Plexus_windows    =mainurl_zips+'P2PStreams_Plexus_Windows.zip'
url_Plexus_android    =mainurl_zips+'P2PStreams_Plexus_Android.zip'
url_Pulsar            =mainurl_zips+'Pulsar.zip'
url_iStream           =mainurl_zips+'iStream.zip'
url_Quasar            =mainurl_zips+'Quasar.zip'
url_repository_Andy   =mainurl+'Andy.repository.zip'
url_superrepo1        =mainurl+'_repo/superrepo.kodi.jarvis.all/superrepo.kodi.jarvis.all-0.7.04.zip'
url_superrepo2        =mainurl+'_repo/superrepo.kodi.isengard.all/superrepo.kodi.isengard.all-0.7.04.zip'
#
url_advancedsettingsetter =mainurl+'_repo/script.advancedsettingsetter/script.advancedsettingsetter-0.0.1.zip'
url_rsseditor             =mainurl+'_repo/script.rss.editor/script.rss.editor-2.0.4.zip'
url_thumbnailscleaner     =mainurl+'_repo/script.thumbnailscleaner/script.thumbnailscleaner-1.1.4.zip'
url_scriptkeymap          =mainurl+'_repo/script.keymap/script.keymap-1.0.9.zip'
#
url_Android_External_Player=mainurl_txt+'playercorefactory.xml'
url_XML_SOURCES          =mainurl_txt+'sources.xml'
url_XML_RSS              =mainurl_txt+'RssFeeds.xml'
url_XML_autoexec         =mainurl_txt+'autoexec.py'
url_XML_PASSWORDS        =mainurl_txt+'passwords.xml'
url_XML_favourites       =mainurl_txt+'favourites.xml'
url_XML_Database         =mainurl_txt+'Database.xml'
url_ZIP_Database         =mainurl_txt+'Database.zip'
url_ZIP_keymaps          =mainurl_txt+'keymaps.zip'
url_XML_ADVANCEDSETTINGS =mainurl_txt+'advancedsettings.xml'

zip          =  ADDON.getSetting('zip')
localcopy    =  ADDON.getSetting('localcopy')
privatebuilds=  ADDON.getSetting('private')
reseller     =  ADDON.getSetting('reseller')
resellername =  ADDON.getSetting('resellername')
resellerid   =  ADDON.getSetting('resellerid')
mastercopy   =  ADDON.getSetting('mastercopy')
username     =  ADDON.getSetting('username')
password     =  ADDON.getSetting('password')
login        =  ADDON.getSetting('login')
trcheck      =  ADDON.getSetting('trcheck')
dialog       =  xbmcgui.Dialog()
dp           =  xbmcgui.DialogProgress()
HOME         =  xbmc.translatePath('special://home/')
USERDATA     =  xbmc.translatePath(os.path.join('special://home/userdata',''))
MEDIA        =  xbmc.translatePath(os.path.join('special://home/media',''))
AUTOEXEC     =  xbmc.translatePath(os.path.join(USERDATA,'autoexec.py'))
AUTOEXECBAK  =  xbmc.translatePath(os.path.join(USERDATA,'autoexec_bak.py'))
ADDON_DATA   =  xbmc.translatePath(os.path.join(USERDATA,'addon_data'))
PLAYLISTS    =  xbmc.translatePath(os.path.join(USERDATA,'playlists'))
DATABASE     =  xbmc.translatePath(os.path.join(USERDATA,'Database'))
THUMBNAILS   =  xbmc.translatePath(os.path.join(USERDATA,'Thumbnails'))
ADDONS       =  xbmc.translatePath(os.path.join('special://home','addons',''))
CBADDONPATH  =  xbmc.translatePath(os.path.join(ADDONS,AddonID,'default.py'))
FANART       =  xbmc.translatePath(os.path.join(ADDONS,AddonID,'fanart.jpg'))
GUISETTINGS  =  os.path.join(USERDATA,'guisettings.xml')
GUI          =  xbmc.translatePath(os.path.join(USERDATA,'guisettings.xml'))
GUIFIX       =  xbmc.translatePath(os.path.join(USERDATA,'guifix.xml'))
INSTALL      =  xbmc.translatePath(os.path.join(USERDATA,'install.xml'))
FAVS         =  xbmc.translatePath(os.path.join(USERDATA,'favourites.xml'))
SOURCE       =  xbmc.translatePath(os.path.join(USERDATA,'sources.xml'))
ADVANCED     =  xbmc.translatePath(os.path.join(USERDATA,'advancedsettings.xml'))
PROFILES     =  xbmc.translatePath(os.path.join(USERDATA,'profiles.xml'))
RSS          =  xbmc.translatePath(os.path.join(USERDATA,'RssFeeds.xml'))
KEYMAPS      =  xbmc.translatePath(os.path.join(USERDATA,'keymaps','keyboard.xml'))
VERSION = "1.0.0"
PATH = "Kodi Maintenance" 


#End My variables paths# No reason to edit below here (no paths to fill)
#-----------------------------------------------------------------------------------------------------------------
xbmc.executebuiltin("Container.SetViewMode(500)")

#def data_check():
#	if not os.path.exists(usrdata): 
#		os.mkdir(usrdata)
#data_check()


# # Open Settings on first run
#if not ADDON.getSetting('already_shown') == 'true':
   #ADDON.openSettings()
#   ADDON.setSetting('already_shown', 'true')


################################
###     Main Menu
################################
def Categories():
    sign = 0
    mainmenu     =  ADDON.getSetting('mainmenu')
    maintenance  =  ADDON.getSetting('maintenance')
    kmintbuilds  =  ADDON.getSetting('kmintbuilds')
    thirdpartybuilds =  ADDON.getSetting('thirdpartybuilds')
#
    #extras.addDir('','Clean All Crap','url','Clean_Crap','clean.png','','','')
    extras.addDir('folder','Clean Crap','none', 'tools', 'clean.png','','','')
    extras.addDir('folder','Add-on Maintenance', 'none', 'addonfixes', 'tweaks.png','','','')
    extras.addDir('folder','AdvancedSettings.xml','none', 'AdvancedSettings_menu', 'advancedsettings.jpg','','','')
    extras.addDir('folder','XML','none','XML_MENU','XML_ALL.png','','','')
    extras.addDir('','View Log', 'none', 'log', 'log.png','','','') 
    extras.addDir('folder','Kodi Info','none','Info_MENU','FAQ.png','','','')
    extras.addDir('','Force Close Kodi','url','kill_kodi','reboot.png','','','')
    extras.addDir('folder','Backup Your Content','none','backup_option','Backup.png','','','')
    extras.addDir('folder','Restore Your Content','none','restore_option','Restore.png','','','')
#
    if mainmenu == 'true': 
        extras.addDir('','Install the following in order as desired','none','warning','order.jpg','','','')
        extras.addDir('','[COLOR green]Install All Extras[/COLOR]','url', 'Install_All', 'Restore_Full.png','','','')
        extras.addDir('','Repos Install',url_Repos,'Repos_Backup','Repos.png','','','')
        extras.addDir('','Addon_Data (App Settings) Install',url_Addon_Data,'Addon_Data_Backup','Addon_Data.png','','','')
        extras.addDir('','Addons Install',url_Addons,'Addons_Backup','Addons.png','','','')
        extras.addDir('','IPTV Addons Install',url_Addons_Video_IPTV,'Addons_Backup_IPTV','IPTV.png','','','')        
        #extras.addDir('','XML Install','url','XML_All_Backup','XML_ALL.png','','','')
#  
    if maintenance == 'true':
        extras.addDir('','Sources.xml (Andy Media shares)',url_XML_Database,'XML_Database','XML_Database.png','','','')
        
    #
    #extras.addDir('folder','[COLOR green]Extra Builds[/COLOR]','none','Extra_Builds','extra_builds.png','','','')
    if thirdpartybuilds == 'true':
        extras.addDir('folder','[COLOR green]Extra Builds[/COLOR]','none','Extra_Builds','extra_builds.png','','','')
#
    if xbmc.getCondVisibility('system.platform.android'): extras.addDir('','Android External Player',url_Android_External_Player,'androidexternalplayer','androidexternalplayer.jpg','','','')
    extras.addDir('folder','Kodi System Settings','none','Kodi_System','Kodi_Settings.png','','','')
    extras.addDir('','Settings (This addon)','url','addon_settings','settings.png','','','')
#



################################
###     Maintenance Menu     ###
################################
def Maintenance_Menu():
    extras.addDir('','View Log', 'none', 'log', 'log.png','','','')  
    extras.addDir('','Clean All Crap','url','Clean_Crap','clean.png','','','')
    extras.addDir('','Fresh Start (Wipe My Install)', 'none', 'wipe_xbmc', 'freshstart.jpg','','','')
    extras.addDir('','Delete Leftovers (Packages Folder)','url','Purge_Packages','package_purge.png','','','')
    #extras.addDir('','Delete Packages (zip)','url','remove_packages','package_purge.png','','','')
    extras.addDir('','Delete Cache','url','clear_cache','clearcache.jpg','','','')
    extras.addDir('','Thumbs GUI', url_thumbnailscleaner, 'script_thumbnailscleaner', 'thumbnailscleaner.png','','','')   
    extras.addDir('','Delete Artwork Cache', 'none', 'remove_textures', 'thumb.png','','','')
    extras.addDir('','Delete File From Device','url','remove_build','delete.jpg','','','')
    extras.addDir('','Fix TV py',TvPy,'Fix_Guide','Fix_Guide.png','','','')
    extras.addDir('','Delete Old Crash Logs','url','remove_crash_logs','eraselogs.jpg','','','')
    extras.addDir('','Help', 'none', 'help', 'help.png','','','')
#


################################
###     Addon_Fixes Menu     ###
################################
def Addon_Fixes_Menu():
    extras.addDir('','Zip Addon Install','url','AddonBrowser','zip.jpg','','','')
    extras.addDir('','Convert Physical Paths To Special (User_Data)',HOME,'fix_special','setpath.jpg','','','')
    extras.addDir('folder','Delete Addon (inc. passwords)','plugin','addon_removal_menu', 'addonremoval.jpg','','','')
    extras.addDir('','Delete Addon_Data','url','remove_addon_data','userdata.png','','','')
    extras.addDir('','Wipe All Add-on Settings (addon_data)','url','remove_addon_data','clean.png','','','')
    extras.addDir('','Update My Add-ons (Force Refresh)', 'none', 'update', 'addon.png','','','')
    extras.addDir('','librtmp.dll', librtmp, 'librtmp', 'librtmp.png','','','')
    extras.addDir('','Hide my add-on passwords','none','hide_passwords', 'Lock.png','','','')
    extras.addDir('','Unhide my add-on passwords','none','unhide_passwords', 'Unlock.png','','','')
    extras.addDir('','Shortcuts (Homescreen)','plugin.','shortcuts','shortcut.jpg','','','')
    extras.addDir('','Andy Repo (Install)',url_repository_Andy,'Andy_Repo','Andy_Repo.png','','','')
    extras.addDir('','Super Repo (Jarvis)',url_superrepo1,'superrepo1','Repo_SuperRepo.png','','','')
    extras.addDir('','Super Repo (Isengard)',url_superrepo2,'superrepo2','Repo_SuperRepo3.png','','','')
    extras.addDir('','Plexus and P2P Streams (Full)',url_Plexus_windows,'Plexus','P2PStreams.jpg','','','')
    extras.addDir('','iStream (Xunitytalk)',url_iStream,'iStream','iStream.png','','','')
    extras.addDir('','Quasar (Slows Kodi)',url_Quasar,'Quasar','Quasar.png','','','')    
    extras.addDir('','Pulsar (Slows Kodi)',url_Pulsar,'Pulsar','Pulsar.png','','','')
    extras.addDir('','Minimal Dependancies','file','Minimal_Dependancies','paramedic.png','','','')
#




################################
###     XML Menu             ###
################################    
def XML_MENU(): 
    extras.addDir('','All xml (Defaults)','url','XML_All_Backup','XML_ALL.png','','','')
    extras.addDir('','Sources.xml (Extra Repos)',url_XML_SOURCES,'XML_SOURCES','XML_SOURCES.png','','','')
    extras.addDir('','View sources.xml','url','view_sources','XML_SOURCES.png','','','')   
    extras.addDir('','Keymap Editor',url_scriptkeymap,'script_keymap_editor','keymaps.png','','','')
    extras.addDir('','Keymaps',url_ZIP_keymaps,'keymaps','keymaps.png','','','')   
    extras.addDir('','RSS Editor',url_rsseditor,'script_rss_editor','rsseditor.png','','','')
    extras.addDir('','RSSFeeds.xml',url_XML_RSS,'XML_RSS','rss.jpg','','','')
    extras.addDir('','View RSSFeeds.xml','url','view_RSSFeeds','rss.jpg','','','')    
    extras.addDir('','favourites.xml',url_XML_favourites,'XML_favourites','fav.png','','','')
    extras.addDir('','View favourites.xml','url','view_favourites','fav.png','','','')
    extras.addDir('','AdvancedSettings.xml (Extra Settings)',mainurl_txt+'advancedsettings.xml','add_advancedsettings','XML_ADVANCEDSETTINGS.png','','','')
    extras.addDir('','View advancedsettings.xml','url','view_advancedxml','XML_ADVANCEDSETTINGS.png','','','')
    extras.addDir('','autoexec.py',url_XML_autoexec,'XML_autoexec','XML.png','','','')
#

################################
###   Advancedsettings Menu  ###
################################    
def AdvancedSettings_MENU(): 
    extras.addDir('','Advancedsettings Edit',url_advancedsettingsetter,'script_advancedsettingsetter','advancedsettingsetter.png','','','')
    extras.addDir('','View advancedsettings.xml','url','view_advancedxml','verifyadvancedsettings.jpg','','','')
    extras.addDir('','Verify advancedsettings.xml','url','verifyadvancedsettings','verifyadvancedsettings.jpg','','','')
    extras.addDir('','Remove advancedsettings.xml','url','removeadvancedsettings','removeadvancedsettings.jpg','','','')
    extras.addDir('','Enable Zero Caching Advanced XML',mainurl_txt+'advancedsettings_0_cache.xml','add_advancedsettings','zerocache.jpg','','','')
    extras.addDir('','Enable Full Advanced XML',mainurl_txt+'advancedsettings.xml','add_advancedsettings','XML_ADVANCEDSETTINGS.png','','','')
    extras.addDir('','Enable 1 Gig Advanced XML',mainurl_txt+'advancedsettings_1Gig_Mem.xml','add_advancedsettings','XML_ADVANCEDSETTINGS.png','','','')
    extras.addDir('','Enable 2 Gig Advanced XML',mainurl_txt+'advancedsettings_2Gig_Mem.xml','add_advancedsettings','XML_ADVANCEDSETTINGS.png','','','')    
    extras.addDir('','Enable 4 Gig Advanced XML',mainurl_txt+'advancedsettings_4Gig_Mem.xml','add_advancedsettings','XML_ADVANCEDSETTINGS.png','','','')    
    extras.addDir('','Enable 8 Gig Advanced XML',mainurl_txt+'advancedsettings_8Gig_Mem.xml','add_advancedsettings','XML_ADVANCEDSETTINGS.png','','','')    
#

################################
###     Info MENU            ###
################################    
def Info_MENU(): 
    extras.addDir('','View Log', 'none', 'log', 'log.png','','','')
    extras.addDir('','IP?','url','get_ip','ip.png','','','')
    extras.addDir('','Check Kodi Version', 'none', 'xbmcversion', 'version.png','','','')
    extras.addDir('','Check Storage', 'none', 'check_storage', 'hdd.png','','','')
    extras.addDir('folder','Speed Test', 'none', 'speed_test', 'speed.png','','','')
    extras.addDir('','News', 'none', 'text_guide', 'news.jpg','','','')
#

################################
###     Kodi_System Menu     ###
################################
def Kodi_System_MENU():
    #http://kodi.wiki/view/Keymaps
    extras.addDir('','Kodi Settings Main','url','systemsettings','settings.png','','','')
    extras.addDir('','File Manager','none','filemanager','file_manager.png','','','')
    extras.addDir('','System Info','url','systeminfo','FAQ.png','','','')
    extras.addDir('','Zip Addon Install','url','AddonBrowser','zip.jpg','','','')
    extras.addDir('','Skin Settings','url','skinsettings','theme.png','','','')
    extras.addDir('','Profiles','url','profiles','Profile.png','','','')
    extras.addDir('','Appearance Settings','url','appearancesettings','thumb.png','','','')
    extras.addDir('','Video Settings','url','videossettings','1.jpg','','','')
    extras.addDir('','PVR Settings','url','pvrsettings','1.jpg','','','')
    extras.addDir('','Music Settings','url','musicsettings','1.jpg','','','')
    extras.addDir('','Weather Settings','url','weathersettings','1.jpg','','','')
    extras.addDir('','Service Settings','url','servicesettings','1.jpg','','','')
    extras.addDir('','Screen Calibration','url','screencalibration','1.jpg','','','')
#

################################
###     Speed test Menu      ###
################################
def Speed_Test_Menu():
    import speedtest
    extras.addDir('','Download 16MB file   - [COLOR=lime]Server 1[/COLOR]', 'https://totalrevolution.googlecode.com/svn/trunk/download%20files/16MB.txt', 'runtest', 'speed.png','','','')
    extras.addDir('','Download 32MB file   - [COLOR=lime]Server 1[/COLOR]', 'https://totalrevolution.googlecode.com/svn/trunk/download%20files/32MB.txt', 'runtest', 'speed.png','','','')
    extras.addDir('','Download 64MB file   - [COLOR=lime]Server 1[/COLOR]', 'https://totalrevolution.googlecode.com/svn/trunk/download%20files/64MB.txt', 'runtest', 'speed.png','','','')
    extras.addDir('','Download 128MB file -  [COLOR=lime]Server 1[/COLOR]', 'https://totalrevolution.googlecode.com/svn/trunk/download%20files/128MB.txt', 'runtest', 'speed.png','','','')
    extras.addDir('','Download 10MB file   - [COLOR=yellow]Server 2[/COLOR]', 'http://www.wswd.net/testdownloadfiles/10MB.zip', 'runtest', 'speed.png','','','')
#

################################
###   Extra Builds Menu      ###
################################
def Extra_Builds_MENU():
    thirdpartybuilds  =  ADDON.getSetting('thirdpartybuilds')
    adultbuilds  =  ADDON.getSetting('adultbuilds')
    guisettings  =  ADDON.getSetting('guisettings')
    kmintbuilds  =  ADDON.getSetting('kmintbuilds')    
    if kmintbuilds == 'true':
        extras.addDir('folder','[COLOR green]Andys Pre-Configured (Default) (Onedrive)[/COLOR]','none', 'kmintmenu', 'Restore_Full.png','','','')
    if thirdpartybuilds == 'true':
        #extras.addDir('folder','[COLOR gold]KodiMaster Builds[/COLOR]','none', 'buildmenu', 'KodiMaster_Builds.png','','','')
        extras.addDir('folder','[COLOR blue]Third-Party Builds[/COLOR]','none', 'thirdpartymenu', 'ThirdParty_Builds.png','','','')
        #extras.addDir('folder','[COLOR gold]KodiMaster International Builds[/COLOR]','none', 'kmintmenu', 'KodiMasterInt_Builds.png','','','')
    if adultbuilds == 'true':
        extras.addDir('folder','[COLOR red]Adult Builds[/COLOR]','none', 'adultmenu', 'Adult_Builds.png','','','')
    guisettings  =  ADDON.getSetting('guisettings')
    if guisettings == 'true':
        extras.addDir('folder','Gui Settings XML','none', 'guisettings', 'ThirdParty_Builds.png','','','')
#



################################
###    Addon removal Menu    ###
################################
def Addon_Removal_Menu():
    for file in glob.glob(os.path.join(ADDONS,'*')):
        name=str(file).replace(ADDONS,'[COLOR=red]REMOVE [/COLOR]').replace('plugin.','[COLOR=dodgerblue](PLUGIN) [/COLOR]').replace('audio.','').replace('video.','').replace('skin.','[COLOR=yellow](SKIN) [/COLOR]').replace('repository.','[COLOR=orange](REPOSITORY) [/COLOR]').replace('script.','[COLOR=cyan](SCRIPT) [/COLOR]').replace('metadata.','[COLOR=gold](METADATA) [/COLOR]').replace('service.','[COLOR=pink](SERVICE) [/COLOR]').replace('weather.','[COLOR=green](WEATHER) [/COLOR]').replace('module.','[COLOR=gold](MODULE) [/COLOR]')
        iconimage=(os.path.join(file,'icon.png'))
        fanart=(os.path.join(file,'fanart.jpg'))
        extras.addDir('',name,file,'remove_addons',iconimage,fanart,'','')
#

################################
###   Function open addon settings
################################
def Addon_Settings():
    ADDON.openSettings(sys.argv[0])
#

################################
###     Function to clear all known cache files
################################
def Clear_Cache():
    choice = xbmcgui.Dialog().yesno('Clear All Known Cache?', 'This will clear all known cache files and can help', 'if you\'re encountering kick-outs during playback.','as well as other random issues. There is no harm in using this.', nolabel='Cancel',yeslabel='Delete')
    if choice == 1:
        cache.Wipe_Cache()
        cache.Remove_Textures()
#

################################
###     Function to clear the addon_data
################################
def Remove_Addon_Data():
    choice = xbmcgui.Dialog().yesno('Delete Addon_Data Folder?', 'This will free up space by deleting your addon_data', 'folder. This contains all addon related settings', 'including username and password info.', nolabel='Cancel',yeslabel='Delete')
    if choice == 1:
        extras.Delete_Userdata()
        dialog.ok("Addon_Data Removed", '', 'Your addon_data folder has now been removed.','')
#

################################
###     Function to Remove_Crash_Logs
################################
def Remove_Crash_Logs():
    choice = xbmcgui.Dialog().yesno('Remove All Crash Logs?', 'There is absolutely no harm in doing this, these are', 'log files generated when Kodi crashes and are','only used for debugging purposes.', nolabel='Cancel',yeslabel='Delete')
    if choice == 1:
        extras.Delete_Logs()
        dialog.ok("Crash Logs Removed", '', 'Your crash log files have now been removed.','')
#

################################
###     Function to clear the packages folder
################################
def Remove_Packages():
    choice = xbmcgui.Dialog().yesno('Delete Packages Folder?', 'This will free up space by deleting the zip install', 'files of your addons. The only downside is you\'ll no', 'longer be able to rollback to older versions.', nolabel='Cancel',yeslabel='Delete')
    if choice == 1:
        extras.Delete_Packages()
        #dialog.ok("Packages Removed", '', 'Your zip install files have now been removed.','')
#

################################
###     Fresh Start (Wipe Kodi)
################################
def Wipe_Kodi():
    zip          =  ADDON.getSetting('zip')
    USB          =  xbmc.translatePath(os.path.join(zip,'Kodi_Backups',''))
    CBPATH       =  xbmc.translatePath(os.path.join(zip,'Kodi_Backups',''))
    cookiepath   =  xbmc.translatePath(os.path.join(ADDON_DATA,AddonID,'cookiejar'))
    startuppath  =  xbmc.translatePath(os.path.join(ADDON_DATA,AddonID,'startup.xml'))
    tempfile     =  xbmc.translatePath(os.path.join(ADDON_DATA,AddonID,'temp.xml'))
    idfile       =  xbmc.translatePath(os.path.join(ADDON_DATA,AddonID,'id.xml'))
    idfiletemp   =  xbmc.translatePath(os.path.join(ADDON_DATA,AddonID,'idtemp.xml'))
    notifyart    =  xbmc.translatePath(os.path.join(ADDONS,AddonID,'resources/'))
    skin         =  xbmc.getSkinDir()
    userdatafolder = xbmc.translatePath(os.path.join(ADDON_DATA,AddonID))
    GUINEW       =  xbmc.translatePath(os.path.join(userdatafolder,'guinew.xml'))
    guitemp      =  xbmc.translatePath(os.path.join(userdatafolder,'guitemp',''))
    tempdbpath   =  xbmc.translatePath(os.path.join(USB,'Database'))
    USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
    #base='http://www.kodimaster.com/'
    #
    os.system('TASKKILL /im pulsar.exe /f');os.system('TASKKILL /im quasar.exe /f')
    mybackuppath = xbmc.translatePath(os.path.join(USB,'Kodi_Backups'))
    choice = xbmcgui.Dialog().yesno("ABSOLUTELY CERTAIN?!!!", 'Are you absolutely certain you want to wipe?', '', 'All addons and settings will be completely wiped!', yeslabel='Yes',nolabel='No')
    if choice == 1:
        if skin!= "skin.confluence":
            dialog.ok(AddonTitle,'Please switch to the default Confluence skin','before performing a wipe.','')
            xbmc.executebuiltin("ActivateWindow(appearancesettings)")
            return
        else:
            choice = xbmcgui.Dialog().yesno("VERY IMPORTANT", 'This will completely wipe your install.', 'Would you like to create a backup before proceeding?', '', yeslabel='No', nolabel='Yes')
            if choice == 0:
                if not os.path.exists(mybackuppath):
                    os.makedirs(mybackuppath)
                vq = extras.Get_Keyboard( heading="Enter a name for this backup" )
                if ( not vq ): return False, 0
                title = urllib.quote_plus(vq)
                backup_zip = xbmc.translatePath(os.path.join(mybackuppath,title+'.zip'))
                exclude_dirs_full =  ['Andy.plugin.program.Maintenance','Andy.repository','script.module.addon.common']
                exclude_files_full = ["xbmc.log","xbmc.old.log","kodi.log","kodi.old.log","kodi.log","kodi.old.log",'.DS_Store','.setup_complete','XBMCHelper.conf']
                message_header = "Creating full backup of existing build"
                message1 = "Archiving..."
                message2 = ""
                message3 = "Please Wait"
                communitybuilds.Archive_Tree(HOME, backup_zip, message_header, message1, message2, message3, exclude_dirs_full, exclude_files_full)
            choice = xbmcgui.Dialog().yesno("Remove "+AddonTitle+"?", 'Do you also want to remove this addon', 'and have a complete fresh start or would you', 'prefer to keep this on your system?', yeslabel='Remove',nolabel='Keep')
            if choice == 0:
                cache.Remove_Textures()
                trpath = xbmc.translatePath(os.path.join(ADDONS,AddonID,''))
                #trtemp = xbmc.translatePath(os.path.join(HOME,'..',AddonID+'.zip'))
                trtemp = xbmc.translatePath(os.path.join(USB,'..',AddonID+'.zip'))
                communitybuilds.Archive_File(trpath, trtemp)
                deppath = xbmc.translatePath(os.path.join(ADDONS,'script.module.addon.common',''))
                #deptemp = xbmc.translatePath(os.path.join(HOME,'..','script.module.addon.common.zip'))
                deptemp = xbmc.translatePath(os.path.join(USB,'..','script.module.addon.common.zip'))
                communitybuilds.Archive_File(deppath, deptemp)
                reppath = xbmc.translatePath(os.path.join(ADDONS,'Andy.repository',''))
                #reptemp = xbmc.translatePath(os.path.join(HOME,'..','Andy.repository.zip'))
                reptemp = xbmc.translatePath(os.path.join(USB,'..','Andy.repository.zip'))
                communitybuilds.Archive_File(reppath, reptemp)
                extras.Destroy_Path(HOME)
                if not os.path.exists(trpath):
                    os.makedirs(trpath)
                if not os.path.exists(deppath):
                    os.makedirs(deppath)
                if not os.path.exists(reppath):
                    os.makedirs(reppath)
                time.sleep(1)
                communitybuilds.Read_Zip(trtemp)
                dp.create(AddonTitle,"Checking ",'', 'Please Wait')
                dp.update(0,"", "Extracting Zip Please Wait")
                extract.all(trtemp,trpath,dp)
                communitybuilds.Read_Zip(deptemp)
                extract.all(deptemp,deppath,dp)
                communitybuilds.Read_Zip(reptemp)
                extract.all(reptemp,reppath,dp)
                dp.update(0,"", "Extracting Zip Please Wait")
                dp.close()
                time.sleep(1)
                killkodi()
            elif choice == 1:
                cache.Remove_Textures()
                extras.Destroy_Path(HOME)
                dp.close()
                killkodi()
            else: return
#

################################
###     Builds Section
################################
def BuildMenu():
    link = OPEN_URL('http://kodimaster.com/wizard/kodimasterbuilds.txt').replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
        addDir(name,url,'wizard',iconimage,fanart,description)
    setView('movies', 'MAIN')
	
def KMIntMenu():
    #link = OPEN_URL('http://kodimaster.com/wizard/kmintbuilds.txt').replace('\n','').replace('\r','')
    link = OPEN_URL(dropboxtxt).replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
        addDir(name,url,'wizard',iconimage,fanart,description)
    setView('movies', 'MAIN')
	
def ThirdPartyMenu():
    link = OPEN_URL('http://kodimaster.com/wizard/thirdpartybuilds.txt').replace('\n','').replace('\r','')
    #link = OPEN_URL(mainurl + '_txt/thirdpartybuilds.txt').replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
        addDir(name,url,'wizard',iconimage,fanart,description)
    setView('movies', 'MAIN')
	
def AdultMenu():
    link = OPEN_URL('http://kodimaster.com/wizard/adultbuilds.txt').replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
        addDir(name,url,'wizard',iconimage,fanart,description)
    setView('movies', 'MAIN')
	
def guisettings():
    link = OPEN_URL('http://kodimaster.com/wizard/guisettings.txt').replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
        addDir(name,url,'wizard',iconimage,fanart,description)
    setView('movies', 'MAIN')
	
def OPEN_URL(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link  
    
def wizard(name,url,description):
    path = xbmc.translatePath(os.path.join('special://home/addons','packages'))
    dp = xbmcgui.DialogProgress()
    dp.create("Install Wizard ","Downloading ",'', 'Please Wait')
    lib=os.path.join(path, name+'.zip')
    try:
       os.remove(lib)
    except:
       pass
    downloader.download(url, lib, dp)
    addonfolder = xbmc.translatePath(os.path.join('special://','home'))
    time.sleep(2)
    dp.update(0,"", "Extracting Zip Please Wait")
    print '======================================='
    print addonfolder
    print '======================================='
    extract.all(lib,addonfolder,dp)
    dialog = xbmcgui.Dialog()
    dialog.ok("DOWNLOAD COMPLETE", 'To ensure all changes are saved you must now close Kodi', 'to force close Kodi. Click ok,', 'DO NOT use the quit/exit options in Kodi.')
    killkodi()
#


################################
###     Kill Kodi
################################
def killkodi():
    dialog = xbmcgui.Dialog()
    choice = 1
    choice = xbmcgui.Dialog().yesno('Force Close Kodi?', 'You are about to force close Kodi', 'This is to retain some tweaks.', nolabel='No, Cancel',yeslabel='Yes, Close')
    if choice == 0:
        xbmc.executebuiltin('ActivateWindow(ShutdownMenu)')
        #xbmc.executebuiltin('Quit')
        return
    elif choice == 1:
        pass
    log_path = xbmc.translatePath('special://logpath')
    #
    #################################
    # Windows and Pulsar and Quasar
    #################################
    if xbmc.getCondVisibility('system.platform.windows'):
        pulsar_path = xbmc.translatePath('special://home/addons/plugin.video.pulsar')
        if os.path.exists(pulsar_path)==True: os.system('start TASKKILL /im pulsar.exe /f');os.system('tskill pulsar.exe')
        #
        quasar_path = xbmc.translatePath('special://home/addons/plugin.video.quasar')
        if os.path.exists(quasar_path)==True: os.system('start TASKKILL /im quasar.exe /f');os.system('tskill quasar.exe')
        #
        xbmc_log_path = os.path.join(log_path, 'kodi.log')
        if os.path.exists(xbmc_log_path)==True: os.system('start TASKKILL /im kodi.exe /f');os.system('tskill Kodi.exe')         
        #               
        xbmc_log_path = os.path.join(log_path, 'smc.log')
        if os.path.exists(xbmc_log_path)==True: os.system('start TASKKILL /im SMC.exe /f');os.system('tskill SMC.exe')
        #    
        xbmc_log_path = os.path.join(log_path, 'xbmc.log')
        if os.path.exists(xbmc_log_path)==True: os.system('start TASKKILL /im xbmc.exe /f');os.system('tskill xbmc.exe')
        #
        xbmc_log_path = os.path.join(log_path, 'tvmc.log')
        if os.path.exists(xbmc_log_path)==True: os.system('start TASKKILL /im TVMC.exe /f');os.system('tskill TVMC.exe')
        #    

    if xbmc.getCondVisibility('system.platform.android'):
        try: os.system('adb shell am force-stop org.kodi')
        except: pass
        try: os.system('adb shell am force-stop org.xbmc.kodi')
        except: pass     
        try: os.system('adb shell am force-stop org.xbmc.xbmc')
        except: pass
        try: os.system('adb shell am force-stop org.xbmc')
        except: pass  
        try: os.system('adb shell am force-stop org.smc')
        except: pass   
        try: os.system('adb shell am force-stop org.tvmc')
        except: pass             
        #

    if xbmc.getCondVisibility('system.platform.linux'):
        try: os.system('killall Kodi')
        except: pass
        try: os.system('killall SMC')
        except: pass
        try: os.system('killall XBMC')
        except: pass
        try: os.system('killall -9 xbmc.bin')
        except: pass
        try: os.system('killall -9 SMC.bin')
        except: pass
        try: os.system('killall -9 kodi.bin')
        except: pass
        #

    if xbmc.getCondVisibility('system.platform.osx'):
        try: os.system('killall -9 Kodi')
        except: pass
        try: os.system('killall -9 SMC')
        except: pass
        try: os.system('killall -9 XBMC')
        except: pass
        #
    if xbmc.getCondVisibility('system.platform.ios'):
        print 'ios'
        #
    if xbmc.getCondVisibility('system.platform.atv2'):
        try: os.system('killall AppleTV')
        except: pass
        #
        print "############   try raspbmc force close  #################" #OSMC / Raspbmc
        try: os.system('sudo initctl stop kodi')
        except: pass
        try: os.system('sudo initctl stop xbmc')
        except: pass
        try: os.system('sudo initctl stop tvmc')
        except: pass
        try: os.system('sudo initctl stop smc')
        except: pass
        #
    else:
        print "############   try raspbmc force close  #################" #OSMC / Raspbmc
        try: os.system('sudo initctl stop kodi')
        except: pass
        try: os.system('sudo initctl stop xbmc')
        except: pass
        try: os.system('sudo initctl stop tvmc')
        except: pass
        try: os.system('sudo initctl stop smc')
        except: pass

        #
    dialog.ok("WARNING", "Force Close was unsuccessful.","Closing Kodi normally...",'')
    #xbmc.executebuiltin('Quit')
    xbmc.executebuiltin('ActivateWindow(ShutdownMenu)')




def platform():
    if xbmc.getCondVisibility('system.platform.android'):
        return 'android'
    elif xbmc.getCondVisibility('system.platform.linux'):
        return 'linux'
    elif xbmc.getCondVisibility('system.platform.windows'):
        return 'windows'
    elif xbmc.getCondVisibility('system.platform.osx'):
        return 'osx'
    elif xbmc.getCondVisibility('system.platform.atv2'):
        return 'atv2'
    elif xbmc.getCondVisibility('system.platform.ios'):
        return 'ios'
#

def addDir(name,url,mode,iconimage,fanart,description):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok
#

################################
###     Purge Packages       ###
################################
def PURGEPACKAGES():
    print '###'+AddonTitle+' - DELETING PACKAGES###'
    packages_cache_path = xbmc.translatePath(os.path.join('special://home/addons/packages', ''))
    try:
        for root, dirs, files in os.walk(packages_cache_path):
            file_count = 0
            file_count += len(files)
        # Count files and give option to delete
            if file_count > 0:
                dialog = xbmcgui.Dialog()
                if dialog.yesno("Delete Package Cache Files", str(file_count) + " files found", "Do you want to delete them?"):
                    for f in files:
                        os.unlink(os.path.join(root, f))
                    for d in dirs:
                        shutil.rmtree(os.path.join(root, d))
                    #dialog = xbmcgui.Dialog()
                    #dialog.ok(AddonTitle, "       Deleting Packages all done")
                else:
                        pass
            else:
                dialog = xbmcgui.Dialog()
                dialog.ok(AddonTitle, "       No Packages to Purge")
    except:
        dialog = xbmcgui.Dialog()
        dialog.ok(AddonTitle, "Error Deleting Packages")
#

################################
###          Get IP           ###
################################
def Get_IP(url='http://www.iplocation.net/',inc=1):
    from addon.common.net import Net
    net=Net()
    xbmc_version=xbmc.getInfoLabel("System.BuildVersion"); version=xbmc_version[:4]; print version
    match=re.compile("<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>").findall(net.http_GET(url).content)
    for ip, region, country, isp in match:
        if inc <2: dialog=xbmcgui.Dialog(); dialog.ok("Your Kodi version is: %s" % version, "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % ip, '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % country, '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % isp)
        inc=inc+1
#

################################
###   Install  XML  with Prompt  
################################
def ADVANCEDXML_PROMPT(url,name,file):
    #import advancedsettings
    from addon.common.net import Net
    net=Net()
    #path = xbmc.translatePath(os.path.join('special://home/userdata',''))
    path = xbmc.translatePath(os.path.join('special://profile',''))
    advance=os.path.join(path, file)
    dialog = xbmcgui.Dialog()
    bak=os.path.join(path, file+'.bak')
    if os.path.exists(bak)==False:
        if dialog.yesno("Back Up Original", 'Have You Backed Up Your '+file+'?','', "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]"):
            print '### '+AddonTitle+' - '+file+'###'
            #path = xbmc.translatePath(os.path.join('special://home/userdata',''))
            path = xbmc.translatePath(os.path.join('special://profile',''))
            advance=os.path.join(path, file)
            try:
                os.remove(advance)
                print '=== Maintenance Tool - REMOVING    '+str(advance)+'    ==='
            except:
                pass
            link=net.http_GET(url).content
            a = open(advance,"w")
            a.write(link)
            a.close()
            print '=== Maintenance Tool - WRITING NEW    '+str(advance)+'    ==='
            dialog = xbmcgui.Dialog()
            dialog.ok(AddonTitle, "       Done Adding new "+file)
    else:
        print '###'+AddonTitle+' - '+file+'###'
        #path = xbmc.translatePath(os.path.join('special://home/userdata',''))
        path = xbmc.translatePath(os.path.join('special://profile',''))
        advance=os.path.join(path, file)
        try:
            os.remove(advance)
            print '=== Maintenance Tool - REMOVING    '+str(advance)+'    ==='
        except:
            pass
        link=net.http_GET(url).content
        a = open(advance,"w")
        a.write(link)
        a.close()
        print '=== Maintenance Tool - WRITING NEW    '+str(advance)+'    ==='
        dialog = xbmcgui.Dialog()
        dialog.ok(AddonTitle, "       Done Adding new "+file)
################################
###       Install  XML       ###
################################
def ADVANCEDXML(url,name,file):
    #import advancedsettings
    from addon.common.net import Net
    net=Net()
    #path = xbmc.translatePath(os.path.join('special://home/userdata',''))
    path = xbmc.translatePath(os.path.join('special://profile',''))
    advance=os.path.join(path, file)
    bak=os.path.join(path, file+'.bak')
    if os.path.exists(bak)==False:
        print '### '+AddonTitle+' - '+file+'###'
        #path = xbmc.translatePath(os.path.join('special://home/userdata',''))
        path = xbmc.translatePath(os.path.join('special://profile',''))
        advance=os.path.join(path, file)
        try:
            os.remove(advance)
            print '=== Maintenance Tool - REMOVING    '+str(advance)+'    ==='
        except:
            pass
        link=net.http_GET(url).content
        a = open(advance,"w")
        a.write(link)
        a.close()
        print '=== Maintenance Tool - WRITING NEW    '+str(advance)+'    ==='
    else:
        print '###'+AddonTitle+' - '+file+'###'
        #path = xbmc.translatePath(os.path.join('special://home/userdata',''))
        path = xbmc.translatePath(os.path.join('special://profile',''))
        advance=os.path.join(path, file)
        try:
            os.remove(advance)
            print '=== Maintenance Tool - REMOVING    '+str(advance)+'    ==='
        except:
            pass
        link=net.http_GET(url).content
        a = open(advance,"w")
        a.write(link)
        a.close()
        print '=== Maintenance Tool - WRITING NEW    '+str(advance)+'    ==='
################################
###       check Advanced XML
################################
def CHECKADVANCEDXML(url,name):
    print '###'+AddonTitle+' - CHECK ADVANCE XML###'
    #path = xbmc.translatePath(os.path.join('special://home/userdata',''))
    path = xbmc.translatePath(os.path.join('special://profile',''))
    advance=os.path.join(path, 'advancedsettings.xml')
    try:
        a=open(advance).read()
        if 'zero' in a:
            name='Zero Caching'
        elif 'tuxen' in a:
            name='TUXENS'
    except:
        name="NO ADVANCED"
    dialog = xbmcgui.Dialog()
    dialog.ok(AddonTitle,"[COLOR yellow]YOU HAVE[/COLOR] "+ name+"[COLOR yellow] SETTINGS SETUP[/COLOR]")
################################
###       delete Advanced XML
################################
def DELETEADVANCEDXML(url):
    print '###'+AddonTitle+' - DELETING ADVANCE XML###'
    #path = xbmc.translatePath(os.path.join('special://home/userdata',''))
    path = xbmc.translatePath(os.path.join('special://profile',''))
    advance=os.path.join(path, 'advancedsettings.xml')
    try:
        os.remove(advance)
        dialog = xbmcgui.Dialog()
        print '=== Maintenance Tool - DELETING    '+str(advance)+'    ==='
        dialog.ok(AddonTitle, "       Remove Advanced Settings Sucessfull")
    except:
        dialog = xbmcgui.Dialog()
        dialog.ok(AddonTitle, "       No Advanced Settings To Remove")
###     End Advanced XML     ###
#

################################
#     Option to open a log
################################
def File_Viewer(path,file):
    log_path = xbmc.translatePath(path)
    log = os.path.join(log_path, file)
    extras.Text_Boxes(file, log)
#

################################
###   Open Kodi Settings     ###
################################
def Open_Kodi_Settings(open_settings):
    #xbmc.executebuiltin("StopScript(%s)" % addon_id)
    #dialog=xbmcgui.Dialog(); dialog.ok(AddonTitle,"This will take you to "+open_settings+" settings menu."," ", "Use the back button to return to the Maintenance Menu.")
    #xbmc.executebuiltin("ActivateWindow(AddonBrowser)")
    xbmc.executebuiltin("ActivateWindow("+open_settings+")")
#

################################
###    Clean_Crap            ### 
################################
def Clean_Crap():
    PURGEPACKAGES()
    #Fix_Guide()
    Remove_Crash_Logs()
    #cache.Remove_Textures()  
    Clear_Cache()

################################
###    Check HDD Path Writeable  
################################
def CheckPath():
    path = xbmc.translatePath(os.path.join(zip,'test'))
    #path = xbmc.translatePath(os.path.join(zip))
    d = xbmcgui.Dialog()
    print path
    try:
        os.makedirs(path)
        os.removedirs(path)
        d.ok('[COLOR=lime]SUCCESS[/COLOR]', 'Great news, the path you chose is writeable.', 'Some of these builds are rather big, we recommend', 'a minimum of 1GB storage space.')
    except:
        d.ok('[COLOR=red]CANNOT WRITE TO PATH[/COLOR]', 'Kodi cannot write to the path you\'ve chosen. Please click OK', 'in the settings menu to save the path then try again.', 'Some devices give false results, we recommend using a USB stick as the backup path.')
#

################################
###   Refresh and Update Addons and repo
################################
def Update_Repo():
	  xbmc.executebuiltin("UpdateAddonRepos")  
	  xbmc.executebuiltin("UpdateLocalAddons")
	  if dialog.yesno("Update Addons", 'Depending on the speed of your device it could take a few minutes for the update to take effect..','', "Open Settings?"):xbmc.executebuiltin("ActivateWindow(Addonbrowser, return)")


################################
###      Shortcuts Install   ###
################################
def SHORTCUTS():
        print '=== Installing Pre-Configured Backup Shortcuts ===';
        link=OPEN_URL(shortcutstxt)
        shorts=re.compile('shortcut="(.+?)"').findall(link)
        for shortname in shorts: xEB('Skin.SetString(%s)'%shortname)
        #xEB('Skin.SetString(CustomBackgroundPath,%s)' %img)
        #xEB('Skin.SetBool(ShowBackgroundVideo)')       ## Set to true so we can later set them to false.
        #xEB('Skin.SetBool(ShowBackgroundVis)')         ## Set to true so we can later set them to false.
        #xEB('Skin.ToggleSetting(ShowBackgroundVideo)') ## Switching from true to false.
        #xEB('Skin.ToggleSetting(ShowBackgroundVis)')   ## Switching from true to false.
        #xEB('general.ToggleSetting(settinglevel)')
        #xEBb('HideBackGroundFanart')
        #xEBb('HideVisualizationFanart')
        xEBb('AutoScroll')
        #xEBS('CustomBackgroundPath',SkinBackGroundImg)
        #xEBb('UseCustomBackground')
        print '=== Installing shortcuts Success ===';
        #dialog=xbmcgui.Dialog(); dialog.ok(AddonTitle,"Done Installing Homescreen Shortcuts") 
###  End Shortcuts Install     ###
#


################################
#     Install All Backups
################################
def Install_All(): 
    dialog = xbmcgui.Dialog()
    if dialog.yesno("Restore Backup?", 'Do you want to restore?','', "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]"):
    
        PATH_ADDON(url_Addon_Data, 'Addon_Data', 'profile/addon_data')
        myplatform = platform()
        print "Platform: " + str(myplatform)
        if myplatform == 'osx': # OSX
            print "############   osx  #################"

        elif myplatform == 'linux': #Linux
            print "############  linux  #################"

        elif myplatform == 'android': # Android  
            print "############   android  #################"
            PATH_ADDON(url_Addon_Data_android, 'Addon_Data_Android', 'profile/addon_data')
        
        elif myplatform == 'windows': # Windows
            print "############   Windows  #################"
            PATH_ADDON(url_Addon_Data_windows, 'Addon_Data_Windows', 'profile/addon_data')
        
        # Strip settings paths to xbox paths
        #communitybuilds.Fix_Special(HOME)
        
        PATH_ADDON(url_Repos, 'Addons_Repos', 'home/addons')
        xbmc.executebuiltin("UpdateAddonRepos")

        SHORTCUTS()
        ADDONS_ALL()

        #path = xbmc.translatePath(os.path.join('special://home/addons/packages',addon))
        path = 'special://home/addons/packages'
        lib=os.path.join(path, '__Addon_Data_Andy.zip')
        try:
            addonfolder=xbmc.translatePath(os.path.join('special://home/userdata','addon_data','')); dp=xbmcgui.DialogProgress(); dp.create("Andy Data", "Extracting "+lib,"Please Wait.")
            extract.all(lib,addonfolder,dp)           
        except:
            pass
            
        dialog = xbmcgui.Dialog()
        if dialog.yesno("Restore XML?", 'Restore and overwrite XMLs?','These are settings and tweaks.', "Answer yes if you dont care."):           
            XML_All()
            
        #Remove_Packages()
        #if dialog.yesno("Done", 'Do you wish to refresh addons?  (Unnessessary)'):
        xbmc.executebuiltin("UpdateLocalAddons()"); xbmc.executebuiltin("UpdateAddonRepos()")
        killkodi()
        #Have beer
#

################################
###    ADDONS_ALL Install    ### 
################################
def ADDONS_ALL():
    #dialog = xbmcgui.Dialog()
    #if dialog.yesno("Restore Backup?", 'Do you want to restore Addons?'):
        PATH_ADDON(url_Addons, 'Addons', 'home/addons')
        PATH_ADDON(url_Addons_Video, 'Addons_Video', 'home/addons')
        
        if dialog.yesno("Restore IPTV?", 'Do you want LiveTV (IPTV)?','', "These are unpredictable but worth it"):
            PATH_ADDON(url_Addons_Video_IPTV, 'Addons_IPTV', 'home/addons')
           
        myplatform = platform()
        print "Platform: " + str(myplatform)
        if myplatform == 'osx': # OSX
            print "############   osx  #################"
            xbmc.executebuiltin("UpdateAddonRepos");xbmc.executebuiltin("UpdateLocalAddons()")
            
        elif myplatform == 'linux': #Linux
            print "############  linux  #################"
            xbmc.executebuiltin("UpdateAddonRepos");xbmc.executebuiltin("UpdateLocalAddons()")
            
        elif myplatform == 'android': # Android  
            print "############   android  #################"
            PATH_ADDON(url_Addons_android, 'Addons_android', 'home/addons')
            #PATH_ADDON(url_Plexus_android, 'Plexus_android', '')
            xbmc.executebuiltin("UpdateAddonRepos");xbmc.executebuiltin("UpdateLocalAddons()")
            
        elif myplatform == 'windows': # Windows
            print "############   Windows  #################"
            PATH_ADDON(url_Addons_windows, 'Addons_windows', 'home/addons')
            xbmc.executebuiltin("UpdateAddonRepos");xbmc.executebuiltin("UpdateLocalAddons()")
            Install_librtmp(librtmp)
            #PATH_ADDON(url_Plexus_windows, 'Plexus_windows', '')

            if dialog.yesno("Restore Quasar? (Pulsar is next)", 'Do you want to restore Quasar?','', "It slows Kodi down a bit, but add torrent streaming support."):
                PATH_ADDON(url_Quasar, 'Quasar', 'home/addons') 
        
            if dialog.yesno("Restore Pulsar? (Old Quasar)", 'Do you want to restore Pulsar?','', "It slows Kodi down a bit, but add torrent streaming support."):
                PATH_ADDON(url_Pulsar, 'Pulsar', 'home/addons')              
         
        #xbmc.executebuiltin("UpdateAddonRepos");xbmc.executebuiltin("UpdateLocalAddons()")
        Remove_Packages()
#

################################
###   PATH_ADDON             ###
################################
def PATH_ADDON(url, addontempname,addonpath):
    pluginpath = os.path.exists(xbmc.translatePath(os.path.join('special://home','addons',"packages",addontempname + ".zip")))
    if pluginpath: #exit #dialog=xbmcgui.Dialog()#; dialog.ok(AddonTitle,addontempname + " is installed.")#; xbmc.executebuiltin("RunAddon(%s)" % addontempname)
        print '=== Installing ' +addontempname+ ' Start ===';
        path=xbmc.translatePath(os.path.join('special://home','addons','packages'))
        lib=os.path.join(path,addontempname+'.zip')
        addonfolder=xbmc.translatePath(os.path.join('special://',addonpath,'')); dp=xbmcgui.DialogProgress(); dp.create(AddonTitle, "Extracting "+addontempname+".zip","Please Wait.")
        extract.all(lib,addonfolder,dp)
        print '=== Installing ' +addontempname+ ' Success ===';  
    else:
        #xbmc.executebuiltin("ActivateWindow(busydialog)")
        print '=== Installing ' +addontempname+ ' Start ===';
        path=xbmc.translatePath(os.path.join('special://home','addons','packages'))
        lib=os.path.join(path,addontempname+'.zip')
        DownloaderClass(url,lib,addontempname)
        time.sleep(1)
        print '=== INSTALLING '+ addontempname +' Addon ===';
        addonfolder=xbmc.translatePath(os.path.join('special://',addonpath,'')); dp=xbmcgui.DialogProgress(); dp.create(AddonTitle, "Extracting "+addontempname+".zip","Please Wait.")
        extract.all(lib,addonfolder,dp)
        print '=== Installing ' +addontempname+ ' Success ===';  
        #xbmc.executebuiltin("Dialog.Close(busydialog)")
#


################################
###   PATH_ADDON_PROMPTS     ###
################################
def PATH_ADDON_PROMPTS(url, addontempname,addonpath):
    pluginpath = os.path.exists(xbmc.translatePath(os.path.join('special://home','addons',"packages",addontempname + ".zip")))
    if pluginpath:
        dialog = xbmcgui.Dialog()
        if dialog.yesno(AddonTitle,addontempname + ' is installed.','', "Try and run " +addontempname+ "?"): xbmc.executebuiltin("RunAddon(%s)" % addontempname)
    else:
        #xbmc.executebuiltin("ActivateWindow(busydialog)")
        print '=== Installing ' +addontempname+ ' Start ===';
        path=xbmc.translatePath(os.path.join('special://home','addons','packages'))
        lib=os.path.join(path,addontempname+'.zip')
        DownloaderClass(url,lib,addontempname)
        print '=== INSTALLING '+ addontempname +' Addon ===';
        addonfolder=xbmc.translatePath(os.path.join('special://',addonpath,'')); dp=xbmcgui.DialogProgress(); dp.create(AddonTitle, "Extracting "+addontempname+".zip","Please Wait.")
        extract.all(lib,addonfolder,dp)
        xbmc.executebuiltin("UpdateAddonRepos()");xbmc.executebuiltin("UpdateLocalAddons()")
        print '=== Installing ' +addontempname+ ' Success ===';
        #xbmc.executebuiltin("Dialog.Close(busydialog)")
        #xbmc.executebuiltin("UpdateAddonRepos");xbmc.executebuiltin("UpdateLocalAddons")
        #dialog=xbmcgui.Dialog(); dialog.ok(AddonTitle,"Done Installing "+addontempname)
        dialog = xbmcgui.Dialog()
        if dialog.yesno(AddonTitle,addontempname + ' is installed.','', "Try and run " +addontempname+ "?"): xbmc.executebuiltin("RunAddon(%s)" % addontempname)
#


################################
###   XML All               ###
################################
def XML_All():
    xbmc.executebuiltin("ActivateWindow(busydialog)")
    ADVANCEDXML(url_XML_SOURCES,name,'sources.xml')
    ADVANCEDXML(url_XML_ADVANCEDSETTINGS,name,'advancedsettings.xml')
    ADVANCEDXML(url_XML_RSS,name,'RssFeeds.xml')
    #ADVANCEDXML(url_XML_favourites,name,'favourites.xml')
    xbmc.executebuiltin("Dialog.Close(busydialog)")  
    #dialog = xbmcgui.Dialog(); dialog.ok(AddonTitle, "    Done Adding Xmls")
#

################################
###   Install ibrtmp         ###
################################
def Install_librtmp(url):
    dialog = xbmcgui.Dialog()
    if dialog.yesno("Restore librtmp?", 'This may help with streams.', 'special://home/system/players/dvdplayer'):
        print '=== Installing ' +url+ ' Start ===';
        path=xbmc.translatePath(os.path.join('special://home','system','players','dvdplayer'))
        #path=xbmc.translatePath(os.path.join('special://','system','players','dvdplayer'))
        lib=os.path.join(path, 'librtmp.dll')
        try:
            os.remove(lib)
        except:
            pass
        try:
            os.makedirs(path)
        except:
            pass
        try:
            DownloaderClass(url,lib,'librtmp.dll') 
            time.sleep(1)
        except:
            pass
#

################################
###   DEPENDANCIES install   ###
################################
def DEPENDANCIES_FILE(file):
        pc_archive=xbmc.translatePath(os.path.join('special://home','addons',AddonID,'resources','help',file+'.zip'))
        pc_addonfolder=xbmc.translatePath(os.path.join('special://home','addons',''))
        if not os.path.exists(xbmc.translatePath(os.path.join('special://home','addons',file))): extract.all(pc_archive,pc_addonfolder)
        xbmc.executebuiltin("UpdateLocalAddons()"); xbmc.executebuiltin("UpdateAddonRepos()")
        #dialog=xbmcgui.Dialog(); dialog.ok(AddonTitle,"Done Installing DEPENDANCIES")       
###   End DEPENDANCIES      ###
#

################################
###   DEPENDANCIES Run install   ###
################################
def DEPENDANCIES_FILE_RUN(file):
        pc_archive=xbmc.translatePath(os.path.join('special://home','addons',AddonID,'resources','help',file+'.zip'))
        pc_addonfolder=xbmc.translatePath(os.path.join('special://home','addons',''))
        if not os.path.exists(xbmc.translatePath(os.path.join('special://home','addons',file))): extract.all(pc_archive,pc_addonfolder)
        xbmc.executebuiltin("UpdateLocalAddons()"); xbmc.executebuiltin("UpdateAddonRepos()")
        dialog = xbmcgui.Dialog()
        if dialog.yesno(AddonTitle,file + ' is installed.','', "Do you wish to run " +file+ "?"): xbmc.executebuiltin("RunAddon(%s)" % file)
#

################################
###   Fix Guide Cache        ###
################################
def Fix_Guide(url):
    print '=== Installing ' +url+ ' Start ===';
    path=xbmc.translatePath(os.path.join('special://home','addons',AddonID))
    lib=os.path.join(path,'Clear_Cache.py')
    try:
        os.remove(lib)
    except:
        pass
    try:
        DownloaderClass(url,lib,'Clear_Cache.py') 
        #time.sleep(1)
    except:
        pass
    try:
        xbmc.executebuiltin("RunScript("+path+"/Clear_Cache.py)")
        #import Fix_Guide
    except:
        pass
    #skin fallback       
    path=xbmc.translatePath(os.path.join('special://','skin'))
    lib=os.path.join(path,'Clear_Cache.py')
    try:
        os.remove(lib)
    except:
        pass
    try:
        DownloaderClass(url,lib,'Clear_Cache.py')
        #xbmc.executebuiltin("RunScript("+path+"/Clear_Cache.py)")
    except:
        pass
           
    dialog = xbmcgui.Dialog();dialog.ok("COMPLETE", 'Clear Cache COMPLETE')







#Get params and clean up into string or integer
def Get_Params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]     
        return param
#
def DownloaderClass(url,dest,dlfile, useReq = False):
    dp = xbmcgui.DialogProgress()
    dp.create(AddonTitle,"Downloading & Copying "+dlfile,'')
    if useReq:
        import urllib2
        req = urllib2.Request(url)
        req.add_header('Referer', 'http://wallpaperswide.com/')
        f       = open(dest, mode='wb')
        resp    = urllib2.urlopen(req)
        content = int(resp.headers['Content-Length'])
        size    = content / 100
        total   = 0
        while True:
            if dp.iscanceled():
                raise Exception("Canceled")
                dp.close()
            chunk = resp.read(size)
            if not chunk:
                f.close()
                break
            f.write(chunk)
            total += len(chunk)
            percent = min(100 * total / content, 100)
            dp.update(percent)
    else:
        urllib.urlretrieve(url,dest,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))
# 
def _pbhook(numblocks, blocksize, filesize, url=None,dp=None):
    try:
        percent = min((numblocks*blocksize*100)/filesize, 100)
        dp.update(percent)
    except:
        percent = 100
        dp.update(percent)
    if dp.iscanceled():
        raise Exception("Canceled")
        dp.close()        
#
def xEB(t): xbmc.executebuiltin(t)
def xEBb(t): xEB('Skin.SetBool(%s)'%t)
def xEBS(t,n): xEB('Skin.SetString(%s,%s)'%(t,n))
def doSetView(s): xbmc.executebuiltin("Container.SetViewMode(%s)" % settings.getSetting(s))
#def OPEN_URL(url): req=urllib2.Request(url); req.add_header('User-Agent','Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'); response=urllib2.urlopen(req); link=response.read(); response.close(); return link

#-----------------------------------------------------------------------------------------------------------------
#Addon starts here
params=Get_Params()
addon_id=None
audioaddons=None
author=None
buildname=None
data_path=None
description=None
DOB=None
email=None
fanart=None
forum=None
iconimage=None
link=None
local=None
messages=None
mode=None
name=None
posts=None
programaddons=None
provider_name=None
repo_id=None
repo_link=None
skins=None
sources=None
updated=None
unread=None
url=None
version=None
video=None
videoaddons=None
welcometext=None
zip_link=None

try:    addon_id=urllib.unquote_plus(params["addon_id"])
except: pass
try:    adult=urllib.unquote_plus(params["adult"])
except: pass
try:    audioaddons=urllib.unquote_plus(params["audioaddons"])
except: pass
try:    author=urllib.unquote_plus(params["author"])
except: pass
try:    buildname=urllib.unquote_plus(params["buildname"])
except: pass
try:    data_path=urllib.unquote_plus(params["data_path"])
except: pass
try:    description=urllib.unquote_plus(params["description"])
except: pass
try:    DOB=urllib.unquote_plus(params["DOB"])
except: pass
try:    email=urllib.unquote_plus(params["email"])
except: pass
try:    fanart=urllib.unquote_plus(params["fanart"])
except: pass
try:    forum=urllib.unquote_plus(params["forum"])
except: pass
try:    guisettingslink=urllib.unquote_plus(params["guisettingslink"])
except: pass
try:    iconimage=urllib.unquote_plus(params["iconimage"])
except: pass
try:    link=urllib.unquote_plus(params["link"])
except: pass
try:    local=urllib.unquote_plus(params["local"])
except: pass
try:    messages=urllib.unquote_plus(params["messages"])
except: pass
try:    mode=str(params["mode"])
except: pass
try:    name=urllib.unquote_plus(params["name"])
except: pass
try:    pictureaddons=urllib.unquote_plus(params["pictureaddons"])
except: pass
try:    posts=urllib.unquote_plus(params["posts"])
except: pass
try:    programaddons=urllib.unquote_plus(params["programaddons"])
except: pass
try:    provider_name=urllib.unquote_plus(params["provider_name"])
except: pass
try:    repo_link=urllib.unquote_plus(params["repo_link"])
except: pass
try:    repo_id=urllib.unquote_plus(params["repo_id"])
except: pass
try:    skins=urllib.unquote_plus(params["skins"])
except: pass
try:    sources=urllib.unquote_plus(params["sources"])
except: pass
try:    updated=urllib.unquote_plus(params["updated"])
except: pass
try:    unread=urllib.unquote_plus(params["unread"])
except: pass
try:    url=urllib.unquote_plus(params["url"])
except: pass
try:    version=urllib.unquote_plus(params["version"])
except: pass
try:    video=urllib.unquote_plus(params["video"])
except: pass
try:    videoaddons=urllib.unquote_plus(params["videoaddons"])
except: pass
try:    zip_link=urllib.unquote_plus(params["zip_link"])
except: pass

print str(PATH)+': '+str(VERSION)
print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "IconImage: "+str(iconimage)


def setView(content, viewType):
    # set content type so library shows more views and info 
    if content:
        xbmcplugin.setContent(int(sys.argv[1]), content)
    if ADDON.getSetting('auto-view')=='true':
        xbmc.executebuiltin("Container.SetViewMode(%s)" % ADDON.getSetting(viewType) )
if mode==None or url==None or len(url)<1:
        Categories()
elif mode == 'addon_removal_menu' : Addon_Removal_Menu()
elif mode == 'addonfix'           : addonfix.fixes()
elif mode == 'addonfixes'         : Addon_Fixes_Menu()
elif mode == 'addonmenu'          : Addon_Menu()
elif mode == 'addon_settings'     : Addon_Settings()
elif mode == 'backup'             : BACKUP()
elif mode == 'backup_option'      : communitybuilds.Backup_Option()
elif mode == 'adultmenu'          : AdultMenu()
elif mode == 'thirdpartymenu'     : ThirdPartyMenu()
elif mode == 'kmintmenu'          : KMIntMenu()
elif mode == 'buildmenu'          : BuildMenu()
elif mode == 'categories'         : Categories()
elif mode == 'clear_cache'        : Clear_Cache()
elif mode == 'community_backup'   : communitybuilds.Community_Backup()
elif mode == 'community_menu'     : communitybuilds.Community_Menu(url,video)        
elif mode == 'description'        : communitybuilds.Description(name,url,buildname,author,version,description,updated,skins,videoaddons,audioaddons,programaddons,pictureaddons,sources,adult)
elif mode == 'fix_special'        : communitybuilds.Fix_Special(url)
elif mode == 'genres'             : Genres(url)
elif mode == 'grab_addons'        : addons.Grab_Addons(url)
elif mode == 'grab_builds_premium': communitybuilds.Grab_Builds_Premium(url)
elif mode == 'guisettingsfix'     : communitybuilds.GUI_Settings_Fix(url,local)
elif mode == 'guisettings'        : guisettings()   
elif mode == 'hide_passwords'     : extras.Hide_Passwords()
elif mode == 'LocalGUIDialog'     : communitybuilds.Local_GUI_Dialog()
elif mode == 'remove_addon_data'  : Remove_Addon_Data()
elif mode == 'remove_addons'      : extras.Remove_Addons(url)
elif mode == 'remove_build'       : extras.Remove_Build()
elif mode == 'remove_crash_logs'  : Remove_Crash_Logs()
elif mode == 'remove_packages'    : Remove_Packages()
elif mode == 'remove_textures'    : cache.Remove_Textures()
elif mode == 'restore'            : extras.RESTORE()
elif mode == 'restore_backup'     : communitybuilds.Restore_Backup_XML(name,url,description)
elif mode == 'restore_local_CB'   : communitybuilds.Restore_Local_Community()
elif mode == 'restore_local_gui'  : communitybuilds.Restore_Local_GUI()
elif mode == 'restore_option'     : communitybuilds.Restore_Option()
elif mode == 'restore_zip'        : communitybuilds.Restore_Zip_File(url)
elif mode == 'restore_community'  : communitybuilds.Restore_Community(name,url,video,description,skins,guisettingslink)
elif mode == 'showinfo'           : communitybuilds.Show_Info(url)
elif mode == 'SortBy'             : extras.Sort_By(BuildURL,type)
elif mode == 'text_guide'         : import Notifications;TypeOfMessage="t"; (NewImage,NewMessage)=Notifications.FetchNews(); Notifications.CheckNews(TypeOfMessage,NewImage,NewMessage,False)
#elif mode == 'text_guide'         : import news;news.Text_Guide(name,url)
elif mode == 'tools'              : Maintenance_Menu()     
elif mode == 'unhide_passwords'   : extras.Unhide_Passwords()
elif mode == 'update'             : Update_Repo()
elif mode == 'user_info'          : Show_User_Info()
elif mode == 'xbmcversion'        : extras.XBMC_Version(url)
elif mode == 'wipe_xbmc'          : Wipe_Kodi()
elif mode == 'wizard'             : wizard(name,url,description)

###Main Menu Andy
elif mode == 'System_Tweaks'      : System_Tweaks_MENU()
elif mode == 'Extra_Builds'       : Extra_Builds_MENU()
elif mode == 'AdvancedSettings_menu' : AdvancedSettings_MENU()
elif mode == 'Kodi_System'        : Kodi_System_MENU()
elif mode == 'XML_MENU'           : XML_MENU()
elif mode == 'Info_MENU'          : Info_MENU()
elif mode == 'backup_restore'     : Backup_Restore_Menu()
#Maintenance
elif mode == 'kill_kodi'          : killkodi()
elif mode == 'Purge_Packages'     : PURGEPACKAGES()
elif mode == 'get_ip'             : Get_IP()
elif mode == 'AddonBrowser'       : Open_Kodi_Settings('AddonBrowser')
#elif mode == 'check_storage'      : CheckPath.CheckPath()
elif mode == 'check_storage'      : CheckPath()
elif mode == 'speed_test'         : Speed_Test_Menu()
elif mode == 'runtest'            : speedtest.runtest(url)
elif mode == 'log'                : extras.Log_Viewer()
#elif mode == 'help'               : File_Viewer('special://logpath', 'kodi.log')
elif mode == 'help'               : File_Viewer('special://home/addons/'+AddonID+'/resources/help', 'help.txt')
elif mode == 'warning'            : File_Viewer('special://home/addons/'+AddonID+'/resources/help', 'warning.txt')
#Backups zip
elif mode == 'Install_All'          : Install_All()
#Backups full
elif mode == 'Repos_Backup'         : PATH_ADDON_PROMPTS(url, 'Repos', 'home/addons');xbmc.executebuiltin("UpdateAddonRepos")
elif mode == 'Addons_Backup_IPTV'   : PATH_ADDON_PROMPTS(url, 'IPTV', 'home/addons')
elif mode == 'Addon_Data_Backup'    : PATH_ADDON_PROMPTS(url, 'Addon_Data', 'profile/addon_data');communitybuilds.Fix_Special(url)
elif mode == 'Addons_Backup'        : ADDONS_ALL()
elif mode == 'XML_All_Backup'       : XML_All();dialog = xbmcgui.Dialog();dialog.ok(AddonTitle, "Done Adding Xmls")

elif mode == 'shortcuts'            : SHORTCUTS(); dialog=xbmcgui.Dialog(); dialog.ok(AddonTitle,"Done Installing Homescreen Shortcuts") 

#Advancedsettings.xml Menu
elif mode == 'verifyadvancedsettings' : CHECKADVANCEDXML(url,name)
elif mode == 'removeadvancedsettings' : DELETEADVANCEDXML(url)
elif mode == 'add_advancedsettings'   : ADVANCEDXML_PROMPT(url,name,'advancedsettings.xml')
#XML
elif mode == 'XML_SOURCES'          : ADVANCEDXML_PROMPT(url,name,'sources.xml')
elif mode == 'XML_ADVANCEDSETTINGS' : ADVANCEDXML_PROMPT(url,name,'advancedsettings.xml')
elif mode == 'XML_RSS'              : ADVANCEDXML_PROMPT(url,name,'RssFeeds.xml')
elif mode == 'XML_favourites'       : ADVANCEDXML_PROMPT(url,name,'favourites.xml')
elif mode == 'XML_autoexec'         : ADVANCEDXML_PROMPT(url,name,'autoexec.py')
elif mode == 'XML_Database'         : ADVANCEDXML_PROMPT(url,name,'sources.xml');ADVANCEDXML(url_XML_favourites,name,'favourites.xml');PATH_ADDON(url_ZIP_Database, 'Database', 'userdata/Database');PATH_ADDON(url_ZIP_keymaps, 'keymaps', 'userdata/keymaps');dialog = xbmcgui.Dialog();dialog.ok(AddonTitle, "       Done Adding other Xmls")
elif mode == 'Log_Analyzer'         : LOGANALYZER(url)
elif mode == 'view_advancedxml'     : File_Viewer('special://profile', 'advancedsettings.xml')
elif mode == 'view_sources'         : File_Viewer('special://profile', 'sources.xml')
elif mode == 'view_RSSFeeds'        : File_Viewer('special://profile', 'RSSFeeds.xml')
elif mode == 'view_favourites'      : File_Viewer('special://profile', 'favourites.xml')
#Kodi Settings
elif mode == 'systemsettings'       : Open_Kodi_Settings('settings')
elif mode == 'filemanager'          : Open_Kodi_Settings('filemanager')
elif mode == 'systeminfo'           : Open_Kodi_Settings('systeminfo')
elif mode == 'screencalibration'    : Open_Kodi_Settings('screencalibration')
elif mode == 'servicesettings'      : Open_Kodi_Settings('servicesettings')
elif mode == 'appearancesettings'   : Open_Kodi_Settings('appearancesettings')
elif mode == 'videossettings'       : Open_Kodi_Settings('videossettings')
elif mode == 'musicsettings'        : Open_Kodi_Settings('musicsettings')
elif mode == 'weathersettings'      : Open_Kodi_Settings('weathersettings')
elif mode == 'profiles'             : Open_Kodi_Settings('profiles')
elif mode == 'skinsettings'         : Open_Kodi_Settings('skinsettings')
elif mode == 'pvrsettings'          : Open_Kodi_Settings('pvrsettings')
elif mode == 'Clean_Crap'           : Clean_Crap()

elif mode == 'superrepo1'           : PATH_ADDON_PROMPTS(url, 'superrepo.kodi.jarvis.all', 'home/addons')
elif mode == 'superrepo2'           : PATH_ADDON_PROMPTS(url, 'superrepo.kodi.isengard.all', 'home/addons')
elif mode == 'Quasar'               : PATH_ADDON_PROMPTS(url, 'plugin.video.quasar', 'home/addons')
elif mode == 'Pulsar'               : PATH_ADDON_PROMPTS(url, 'plugin.video.pulsar', 'home/addons')
elif mode == 'Plexus'               : PATH_ADDON_PROMPTS(url, 'program.plexus', 'home')
elif mode == 'iStream'              : PATH_ADDON_PROMPTS(url, 'script.icechannel', 'home')
elif mode == 'Andy_Repo'            : PATH_ADDON_PROMPTS(url, 'Andy.repository', 'home/addons')
elif mode == 'librtmp'              : Install_librtmp(librtmp);dialog = xbmcgui.Dialog();dialog.ok("COMPLETE", 'librtmp COMPLETE')
elif mode == 'keymaps'              : PATH_ADDON(url, 'keymaps', 'userdata/keymaps')
#elif mode == 'script_advancedsettingsetter' : PATH_ADDON(url, 'script.module.xmltodict', 'home/addons');PATH_ADDON_PROMPTS(url, 'script.advancedsettingsetter', 'home/addons')
#elif mode == 'script_advancedsettingsetter' : DEPENDANCIES_FILE('script.module.xmltodict');PATH_ADDON_PROMPTS(url, 'script.advancedsettingsetter', 'home/addons')
#elif mode == 'script_rss_editor'        : PATH_ADDON_PROMPTS(url, 'script.rss.editor', 'home/addons')
#elif mode == 'script_thumbnailscleaner' : PATH_ADDON_PROMPTS(url, 'script.thumbnailscleaner', 'home/addons')
#elif mode == 'script_keymap_editor'     : PATH_ADDON_PROMPTS(url, 'script.keymap', 'home/addons')
#
elif mode == 'script_advancedsettingsetter' : DEPENDANCIES_FILE('script.module.xmltodict');DEPENDANCIES_FILE_RUN('script.advancedsettingsetter')
elif mode == 'script_rss_editor'            : DEPENDANCIES_FILE_RUN('script.rss.editor')
elif mode == 'script_thumbnailscleaner'     : DEPENDANCIES_FILE_RUN('script.thumbnailscleaner')
elif mode == 'script_keymap_editor'         : DEPENDANCIES_FILE_RUN('script.keymap')
#
elif mode == 'Minimal_Dependancies' : DEPENDANCIES_FILE('script.module.addon.common');DEPENDANCIES_FILE('script.module.xmltodict');DEPENDANCIES_FILE('script.keymap');DEPENDANCIES_FILE('script.rss.editor');DEPENDANCIES_FILE('script.thumbnailscleaner');dialog=xbmcgui.Dialog(); dialog.ok(AddonTitle,"Done Installing DEPENDANCIES"); xbmc.executebuiltin("UpdateAddonRepos()");xbmc.executebuiltin("UpdateLocalAddons()")
#elif mode == 'Fix_Guide'            : import Fix_Guide;Fix_Guide.TVGuide(url)
elif mode == 'Fix_Guide'            : Fix_Guide(url)

xbmcplugin.endOfDirectory(int(sys.argv[1]))

			