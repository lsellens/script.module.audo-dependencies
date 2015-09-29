# Detect machine architecture and prepare execution environment
import os
import xbmc
import xbmcaddon
import xbmcvfs

__addon__             = xbmcaddon.Addon(id='script.module.audo-dependencies')
__dependancies__      = xbmc.translatePath(__addon__.getAddonInfo('path'))

parch                         = os.uname()[4]
pnamemapper                   = xbmc.translatePath(__dependancies__ + '/lib/Cheetah/_namemapper.so')
pssl                          = xbmc.translatePath(__dependancies__ + '/lib/OpenSSL/SSL.so')
prand                         = xbmc.translatePath(__dependancies__ + '/lib/OpenSSL/rand.so')
pcrypto                       = xbmc.translatePath(__dependancies__ + '/lib/OpenSSL/crypto.so')
plibcrypto                    = xbmc.translatePath(__dependancies__ + '/lib/OpenSSL/libcrypto.so.1.0.0')
plibssl                       = xbmc.translatePath(__dependancies__ + '/lib/OpenSSL/libssl.so.1.0.0')
plibcryptolk                  = xbmc.translatePath(__dependancies__ + '/lib/libcrypto.so.1.0.0')
plibssllk                     = xbmc.translatePath(__dependancies__ + '/lib/libssl.so.1.0.0')
pyenc                         = xbmc.translatePath(__dependancies__ + '/lib/_yenc.so')
ppar2                         = xbmc.translatePath(__dependancies__ + '/bin/par2')
punrar                        = xbmc.translatePath(__dependancies__ + '/bin/unrar')

xbmc.log('AUDO: ' + parch + ' architecture detected', level=xbmc.LOGDEBUG)

if xbmcvfs.exists(xbmc.translatePath(__dependancies__ + '/arch.x86_64')):
    xbmcvfs.delete(xbmc.translatePath(__dependancies__ + '/arch.x86_64'))
if xbmcvfs.exists(xbmc.translatePath(__dependancies__ + '/arch.armv6l')):
    xbmcvfs.delete(xbmc.translatePath(__dependancies__ + '/arch.armv6l'))
if xbmcvfs.exists(xbmc.translatePath(__dependancies__ + '/arch.armv7l')):
    xbmcvfs.delete(xbmc.translatePath(__dependancies__ + '/arch.armv7l'))

try:
    if xbmcvfs.exists(pnamemapper):
        xbmcvfs.delete(pnamemapper)
    fnamemapper = xbmc.translatePath(__dependancies__ + '/lib/multiarch/_namemapper.so.' + parch)
    xbmcvfs.copy(fnamemapper, pnamemapper)
    os.chmod(pnamemapper, 0755)
    xbmc.log('AUDO: Copied _namemapper.so for ' + parch, level=xbmc.LOGDEBUG)
except Exception, e:
    xbmc.log('AUDO: Error Copying _namemapper.so for ' + parch, level=xbmc.LOGERROR)
    xbmc.log(str(e), level=xbmc.LOGERROR)

try:
    if xbmcvfs.exists(pssl):
        xbmcvfs.delete(pssl)
    fssl = xbmc.translatePath(__dependancies__ + '/lib/multiarch/SSL.so.' + parch)
    xbmcvfs.copy(fssl, pssl)
    os.chmod(pssl, 0755)
    xbmc.log('AUDO: Copied SSL.so for ' + parch, level=xbmc.LOGDEBUG)
except Exception, e:
    xbmc.log('AUDO: Error Copying SSL.so for ' + parch, level=xbmc.LOGERROR)
    xbmc.log(str(e), level=xbmc.LOGERROR)

try:
    if xbmcvfs.exists(prand):
        xbmcvfs.delete(prand)
    frand = xbmc.translatePath(__dependancies__ + '/lib/multiarch/rand.so.' + parch)
    xbmcvfs.copy(frand, prand)
    os.chmod(prand, 0755)
    xbmc.log('AUDO: Copied rand.so for ' + parch, level=xbmc.LOGDEBUG)
except Exception, e:
    xbmc.log('AUDO: Error Copying rand.so for ' + parch, level=xbmc.LOGERROR)
    xbmc.log(str(e), level=xbmc.LOGERROR)

try:
    if xbmcvfs.exists(pcrypto):
        xbmcvfs.delete(pcrypto)
    fcrypto = xbmc.translatePath(__dependancies__ + '/lib/multiarch/crypto.so.' + parch)
    xbmcvfs.copy(fcrypto, pcrypto)
    os.chmod(pcrypto, 0755)
    xbmc.log('AUDO: Copied crypto.so for ' + parch, level=xbmc.LOGDEBUG)
except Exception, e:
    xbmc.log('AUDO: Error Copying crypto.so for ' + parch, level=xbmc.LOGERROR)
    xbmc.log(str(e), level=xbmc.LOGERROR)

try:
    if xbmcvfs.exists(plibcrypto):
        xbmcvfs.delete(plibcrypto)
    flibcrypto = xbmc.translatePath(__dependancies__ + '/lib/multiarch/libcrypto.so.1.0.0.' + parch)
    xbmcvfs.copy(flibcrypto, plibcrypto)
    os.chmod(plibcrypto, 0755)
    os.symlink(plibcrypto, plibcryptolk)
    xbmc.log('AUDO: Copied libcrypto for ' + parch, level=xbmc.LOGDEBUG)
except Exception, e:
    xbmc.log('AUDO: Error Copying libcrypto for ' + parch, level=xbmc.LOGERROR)
    xbmc.log(str(e), level=xbmc.LOGERROR)

try:
    if xbmcvfs.exists(plibssl):
        xbmcvfs.delete(plibssl)
    flibssl = xbmc.translatePath(__dependancies__ + '/lib/multiarch/libssl.so.1.0.0.' + parch)
    xbmcvfs.copy(flibssl, plibssl)
    os.chmod(plibssl, 0755)
    os.symlink(plibssl, plibssllk)
    xbmc.log('AUDO: Copied libssl for ' + parch, level=xbmc.LOGDEBUG)
except Exception, e:
    xbmc.log('AUDO: Error Copying libssl for ' + parch, level=xbmc.LOGERROR)
    xbmc.log(str(e), level=xbmc.LOGERROR)

try:
    if xbmcvfs.exists(pyenc):
        xbmcvfs.delete(pyenc)
    fyenc = xbmc.translatePath(__dependancies__ + '/lib/multiarch/_yenc.so.' + parch)
    xbmcvfs.copy(fyenc, pyenc)
    os.chmod(pyenc, 0755)
    xbmc.log('AUDO: Copied _yenc.so for ' + parch, level=xbmc.LOGDEBUG)
except Exception, e:
    xbmc.log('AUDO: Error Copying _yenc.so for ' + parch, level=xbmc.LOGERROR)
    xbmc.log(str(e), level=xbmc.LOGERROR)

try:
    if xbmcvfs.exists(ppar2):
        xbmcvfs.delete(ppar2)
    fpar2 = xbmc.translatePath(__dependancies__ + '/lib/multiarch/par2.' + parch)
    xbmcvfs.copy(fpar2, ppar2)
    os.chmod(ppar2, 0755)
    xbmc.log('AUDO: Copied par2 for ' + parch, level=xbmc.LOGDEBUG)
except Exception, e:
    xbmc.log('AUDO: Error Copying par2 for ' + parch, level=xbmc.LOGERROR)
    xbmc.log(str(e), level=xbmc.LOGERROR)

try:
    if xbmcvfs.exists(punrar):
        xbmcvfs.delete(punrar)
    funrar = xbmc.translatePath(__dependancies__ + '/lib/multiarch/unrar.' + parch)
    xbmcvfs.copy(funrar, punrar)
    os.chmod(punrar, 0755)
    xbmc.log('AUDO: Copied unrar for ' + parch, level=xbmc.LOGDEBUG)
except Exception, e:
    xbmc.log('AUDO: Error Copying unrar for ' + parch, level=xbmc.LOGERROR)
    xbmc.log(str(e), level=xbmc.LOGERROR)

xbmcvfs.File(xbmc.translatePath(__dependancies__ + '/arch.' + parch), 'w').close()
