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
pyenc                         = xbmc.translatePath(__dependancies__ + '/lib/_yenc.so')
ppar2                         = xbmc.translatePath(__dependancies__ + '/bin/par2')
punrar                        = xbmc.translatePath(__dependancies__ + '/bin/unrar')

xbmc.log('AUDO: ' + parch + ' architecture detected', level=xbmc.LOGDEBUG)

if xbmcvfs.exists(xbmc.translatePath(__dependancies__ + '/arch.i686')):
    xbmcvfs.delete(xbmc.translatePath(__dependancies__ + '/arch.i686'))
if xbmcvfs.exists(xbmc.translatePath(__dependancies__ + '/arch.x86_64')):
    xbmcvfs.delete(xbmc.translatePath(__dependancies__ + '/arch.x86_64'))
if xbmcvfs.exists(xbmc.translatePath(__dependancies__ + '/arch.armv6l')):
    xbmcvfs.delete(xbmc.translatePath(__dependancies__ + '/arch.armv6l'))
if xbmcvfs.exists(xbmc.translatePath(__dependancies__ + '/arch.armv7l')):
    xbmcvfs.delete(xbmc.translatePath(__dependancies__ + '/arch.armv7l'))

try:
    fnamemapper = xbmc.translatePath(__dependancies__ + '/lib/multiarch/_namemapper.so.' + parch)
    xbmcvfs.copy(fnamemapper, pnamemapper)
    xbmc.log('AUDO: Copied _namemapper.so for ' + parch, level=xbmc.LOGDEBUG)
except Exception, e:
    xbmc.log('AUDO: Error Copying _namemapper.so for ' + parch, level=xbmc.LOGERROR)
    xbmc.log(str(e), level=xbmc.LOGERROR)

try:
    fssl = xbmc.translatePath(__dependancies__ + '/lib/multiarch/SSL.so.' + parch)
    xbmcvfs.copy(fssl, pssl)
    xbmc.log('AUDO: Copied SSL.so for ' + parch, level=xbmc.LOGDEBUG)
except Exception, e:
    xbmc.log('AUDO: Error Copying SSL.so for ' + parch, level=xbmc.LOGERROR)
    xbmc.log(str(e), level=xbmc.LOGERROR)

try:
    frand = xbmc.translatePath(__dependancies__ + '/lib/multiarch/rand.so.' + parch)
    xbmcvfs.copy(frand, prand)
    xbmc.log('AUDO: Copied rand.so for ' + parch, level=xbmc.LOGDEBUG)
except Exception, e:
    xbmc.log('AUDO: Error Copying rand.so for ' + parch, level=xbmc.LOGERROR)
    xbmc.log(str(e), level=xbmc.LOGERROR)

try:
    fcrypto = xbmc.translatePath(__dependancies__ + '/lib/multiarch/crypto.so.' + parch)
    xbmcvfs.copy(fcrypto, pcrypto)
    xbmc.log('AUDO: Copied crypto.so for ' + parch, level=xbmc.LOGDEBUG)
except Exception, e:
    xbmc.log('AUDO: Error Copying crypto.so for ' + parch, level=xbmc.LOGERROR)
    xbmc.log(str(e), level=xbmc.LOGERROR)

try:
    fyenc = xbmc.translatePath(__dependancies__ + '/lib/multiarch/_yenc.so.' + parch)
    xbmcvfs.copy(fyenc, pyenc)
    xbmc.log('AUDO: Copied _yenc.so for ' + parch, level=xbmc.LOGDEBUG)
except Exception, e:
    xbmc.log('AUDO: Error Copying _yenc.so for ' + parch, level=xbmc.LOGERROR)
    xbmc.log(str(e), level=xbmc.LOGERROR)

try:
    fpar2 = xbmc.translatePath(__dependancies__ + '/lib/multiarch/par2.' + parch)
    xbmcvfs.copy(fpar2, ppar2)
    os.chmod(ppar2, 0755)
    xbmc.log('AUDO: Copied par2 for ' + parch, level=xbmc.LOGDEBUG)
except Exception, e:
    xbmc.log('AUDO: Error Copying par2 for ' + parch, level=xbmc.LOGERROR)
    xbmc.log(str(e), level=xbmc.LOGERROR)

try:
    funrar = xbmc.translatePath(__dependancies__ + '/lib/multiarch/unrar.' + parch)
    xbmcvfs.copy(funrar, punrar)
    os.chmod(punrar, 0755)
    xbmc.log('AUDO: Copied unrar for ' + parch, level=xbmc.LOGDEBUG)
except Exception, e:
    xbmc.log('AUDO: Error Copying unrar for ' + parch, level=xbmc.LOGERROR)
    xbmc.log(str(e), level=xbmc.LOGERROR)

xbmcvfs.File(xbmc.translatePath(__dependancies__ + '/arch.' + parch), 'w').close()
