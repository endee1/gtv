#
# Copyright (C) 2014 Sean Poyser and Richard Dean (write2dixie@gmail.com)
#
#
#      Modified for tecbox Guide (02/2015 onwards)
#
# This Program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2, or (at your option)
# any later version.
#
# This Program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with XBMC; see the file COPYING. If not, write to
# the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
# http://www.gnu.org/copyleft/gpl.html
#
import time
import os
import xbmc
import xbmcgui
import xbmcaddon


		
def deleteDB():
    try:
        xbmc.log("[script.gtvtvguide] Deleting guide data xml files...", xbmc.LOGDEBUG)
        dbPath2 = xbmc.translatePath(xbmcaddon.Addon(id = 'script.gtvtvguide').getAddonInfo('profile'))
        dbPath2 = os.path.join(dbPath2, 'guide.xml')

        delete_file(dbPath2)

        passed = not os.path.exists(dbPath2)

        if passed:
            xbmc.log("[script.gtvtvguide] Deleting guide data xml files...PASSED", xbmc.LOGDEBUG)
        else:
            xbmc.log("[script.gtvtvguide] Deleting guide data xml files...FAILED", xbmc.LOGDEBUG)

        return passed

    except Exception, e:
        xbmc.log('[script.gtvtvguide] Deleting guide data xml files...EXCEPTION', xbmc.LOGDEBUG)
        return False
		
def delete_file(filename):
    tries = 10
    while os.path.exists(filename) and tries > 0:
        try:
            os.remove(filename)
            break
        except:
            tries -= 1

if __name__ == '__main__':
    if deleteDB():
        d = xbmcgui.Dialog()
        d.ok('gtvtvguide', 'Deleting guide data xml files successfully completed.', 'It will be re-created next time you start the guide')
    else:
        d = xbmcgui.Dialog()
        d.ok('gtvtvguide', 'Deleting guide data xml files Failed.', 'files may be locked,', 'please restart XBMC and try again')
		
time.sleep(1)

def deleteDB():
    try:
        xbmc.log("[script.gtvtvguide] Deleting guide data xml files...", xbmc.LOGDEBUG)
        dbPath3 = xbmc.translatePath(xbmcaddon.Addon(id = 'script.gtvtvguide').getAddonInfo('profile'))
        dbPath3 = os.path.join(dbPath3, 'guide2.xml')

        delete_file(dbPath3)

        passed = not os.path.exists(dbPath3)

        if passed:
            xbmc.log("[script.gtvtvguide] Deleting guide data xml files...PASSED", xbmc.LOGDEBUG)
        else:
            xbmc.log("[script.gtvtvguide] Deleting guide data xml files...FAILED", xbmc.LOGDEBUG)

        return passed

    except Exception, e:
        xbmc.log('[script.gtvtvguide] Deleting guide data xml files...EXCEPTION', xbmc.LOGDEBUG)
        return False

def delete_file(filename):
    tries = 10
    while os.path.exists(filename) and tries > 0:
        try:
            os.remove(filename)
            break
        except:
            tries -= 1

if __name__ == '__main__':
    if deleteDB():
        d = xbmcgui.Dialog()
        d.ok('gtvtvguide', 'Deleting guide data xml files successfully completed.', 'It will be re-created next time you start the guide')
    else:
        d = xbmcgui.Dialog()
        d.ok('gtvtvguide', 'Deleting guide data xml files Failed.', 'files may be locked,', 'please restart XBMC and try again')
		
time.sleep(1)

def deleteDB():
    try:
        xbmc.log("[script.gtvtvguide] Deleting guide data xml files...", xbmc.LOGDEBUG)
        dbPath4 = xbmc.translatePath(xbmcaddon.Addon(id = 'script.gtvtvguide').getAddonInfo('profile'))
        dbPath4 = os.path.join(dbPath4, 'guide3.xmltv')

        delete_file(dbPath4)

        passed = not os.path.exists(dbPath4)

        if passed:
            xbmc.log("[script.gtvtvguide] Deleting guide data xml files...PASSED", xbmc.LOGDEBUG)
        else:
            xbmc.log("[script.gtvtvguide] Deleting guide data xml files...FAILED", xbmc.LOGDEBUG)

        return passed

    except Exception, e:
        xbmc.log('[script.gtvtvguide] Deleting guide data xml files...EXCEPTION', xbmc.LOGDEBUG)
        return False
		
def delete_file(filename):
    tries = 10
    while os.path.exists(filename) and tries > 0:
        try:
            os.remove(filename)
            break
        except:
            tries -= 1

if __name__ == '__main__':
    if deleteDB():
        d = xbmcgui.Dialog()
        d.ok('gtvtvguide', 'Deleting guide data xml files successfully completed.', 'It will be re-created next time you start the guide')
    else:
        d = xbmcgui.Dialog()
        d.ok('gtvtvguide', 'Deleting guide data xml files Failed.', 'files may be locked,', 'please restart XBMC and try again')
		
time.sleep(1)

def deleteDB():
    try:
        xbmc.log("[script.gtvtvguide] Deleting guide data xml files...", xbmc.LOGDEBUG)
        dbPath5 = xbmc.translatePath(xbmcaddon.Addon(id = 'script.gtvtvguide').getAddonInfo('profile'))
        dbPath5 = os.path.join(dbPath5, 'uk1.xml')

        delete_file(dbPath5)

        passed = not os.path.exists(dbPath5)

        if passed:
            xbmc.log("[script.gtvtvguide] Deleting guide data xml files...PASSED", xbmc.LOGDEBUG)
        else:
            xbmc.log("[script.gtvtvguide] Deleting guide data xml files...FAILED", xbmc.LOGDEBUG)

        return passed

    except Exception, e:
        xbmc.log('[script.gtvtvguide] Deleting guide data xml files...EXCEPTION', xbmc.LOGDEBUG)
        return False
		
def delete_file(filename):
    tries = 10
    while os.path.exists(filename) and tries > 0:
        try:
            os.remove(filename)
            break
        except:
            tries -= 1

if __name__ == '__main__':
    if deleteDB():
        d = xbmcgui.Dialog()
        d.ok('gtvtvguide', 'Deleting guide data xml files successfully completed.', 'It will be re-created next time you start the guide')
    else:
        d = xbmcgui.Dialog()
        d.ok('gtvtvguide', 'Deleting guide data xml files Failed.', 'files may be locked,', 'please restart XBMC and try again')
		
time.sleep(1)

def deleteDB():
    try:
        xbmc.log("[script.gtvtvguide] Deleting guide data xml files...", xbmc.LOGDEBUG)
        dbPath6 = xbmc.translatePath(xbmcaddon.Addon(id = 'script.gtvtvguide').getAddonInfo('profile'))
        dbPath6 = os.path.join(dbPath6, 'guide5.xml')

        delete_file(dbPath6)

        passed = not os.path.exists(dbPath6)

        if passed:
            xbmc.log("[script.gtvtvguide] Deleting guide data xml files...PASSED", xbmc.LOGDEBUG)
        else:
            xbmc.log("[script.gtvtvguide] Deleting guide data xml files...FAILED", xbmc.LOGDEBUG)

        return passed

    except Exception, e:
        xbmc.log('[script.gtvtvguide] Deleting guide data xml files...EXCEPTION', xbmc.LOGDEBUG)
        return False
		
def delete_file(filename):
    tries = 10
    while os.path.exists(filename) and tries > 0:
        try:
            os.remove(filename)
            break
        except:
            tries -= 1

if __name__ == '__main__':
    if deleteDB():
        d = xbmcgui.Dialog()
        d.ok('gtvtvguide', 'Deleting guide data xml files successfully completed.', 'It will be re-created next time you start the guide')
    else:
        d = xbmcgui.Dialog()
        d.ok('gtvtvguide', 'Deleting guide data xml files Failed.', 'files may be locked,', 'please restart XBMC and try again')
		

time.sleep(1)