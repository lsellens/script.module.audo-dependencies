# Detect machine architecture and prepare execution environment
import os
import xbmc
import xbmcaddon
import xbmcvfs

__addon__        = xbmcaddon.Addon(id='script.module.audo-dependencies')
__dependencies__ = xbmc.translatePath(__addon__.getAddonInfo('path'))

parch            = os.uname()[4]
pnamemapper      = xbmc.translatePath(__dependencies__ + '/lib/Cheetah/_namemapper.so')
pobjectify       = xbmc.translatePath(__dependencies__ + '/lib/lxml/objectify.so')
petree           = xbmc.translatePath(__dependencies__ + '/lib/lxml/etree.so')
p_constant_time  = xbmc.translatePath(__dependencies__ + '/lib/cryptography/hazmat/bindings/_constant_time.so')
p_openssl        = xbmc.translatePath(__dependencies__ + '/lib/cryptography/hazmat/bindings/_openssl.so')
p_padding        = xbmc.translatePath(__dependencies__ + '/lib/cryptography/hazmat/bindings/_padding.so')
plibcrypto       = xbmc.translatePath(__dependencies__ + '/lib/OpenSSL/libcrypto.so.1.0.0')
plibssl          = xbmc.translatePath(__dependencies__ + '/lib/OpenSSL/libssl.so.1.0.0')
plibcryptolk     = xbmc.translatePath(__dependencies__ + '/lib/libcrypto.so.1.0.0')
plibssllk        = xbmc.translatePath(__dependencies__ + '/lib/libssl.so.1.0.0')
plibffi          = xbmc.translatePath(__dependencies__ + '/lib/libffi.so.6.0.4')
plibffilk        = xbmc.translatePath(__dependencies__ + '/lib/libffi.so.6')
p_cffi_backend   = xbmc.translatePath(__dependencies__ + '/lib/_cffi_backend.so')
pyenc            = xbmc.translatePath(__dependencies__ + '/lib/_yenc.so')
psabyenc         = xbmc.translatePath(__dependencies__ + '/lib/sabyenc.so')
plibgomp         = xbmc.translatePath(__dependencies__ + '/lib/libgomp.so.1')
ppar2            = xbmc.translatePath(__dependencies__ + '/bin/par2')
punrar           = xbmc.translatePath(__dependencies__ + '/bin/unrar')
p7za             = xbmc.translatePath(__dependencies__ + '/bin/7za')

xbmc.log('AUDO: ' + parch + ' architecture detected', level=xbmc.LOGDEBUG)

if xbmcvfs.exists(xbmc.translatePath(__dependencies__ + '/arch.x86_64')):
    xbmcvfs.delete(xbmc.translatePath(__dependencies__ + '/arch.x86_64'))
if xbmcvfs.exists(xbmc.translatePath(__dependencies__ + '/arch.armv6l')):
    xbmcvfs.delete(xbmc.translatePath(__dependencies__ + '/arch.armv6l'))
if xbmcvfs.exists(xbmc.translatePath(__dependencies__ + '/arch.armv7l')):
    xbmcvfs.delete(xbmc.translatePath(__dependencies__ + '/arch.armv7l'))

try:
    if xbmcvfs.exists(pnamemapper):
        xbmcvfs.delete(pnamemapper)
    fnamemapper = xbmc.translatePath(__dependencies__ + '/lib/multiarch/_namemapper.so.' + parch)
    xbmcvfs.copy(fnamemapper, pnamemapper)
    xbmc.log('AUDO: Copied _namemapper.so for ' + parch, level=xbmc.LOGDEBUG)
except Exception, e:
    xbmc.log('AUDO: Error Copying _namemapper.so for ' + parch, level=xbmc.LOGERROR)
    xbmc.log(str(e), level=xbmc.LOGERROR)

try:
    if xbmcvfs.exists(pobjectify):
        xbmcvfs.delete(pobjectify)
    fobjectify = xbmc.translatePath(__dependencies__ + '/lib/multiarch/objectify.so.' + parch)
    xbmcvfs.copy(fobjectify, pobjectify)
    xbmc.log('AUDO: Copied objectify.so for ' + parch, level=xbmc.LOGDEBUG)
except Exception, e:
    xbmc.log('AUDO: Error Copying objectify.so for ' + parch, level=xbmc.LOGERROR)
    xbmc.log(str(e), level=xbmc.LOGERROR)

try:
    if xbmcvfs.exists(petree):
        xbmcvfs.delete(petree)
    fetree = xbmc.translatePath(__dependencies__ + '/lib/multiarch/etree.so.' + parch)
    xbmcvfs.copy(fetree, petree)
    xbmc.log('AUDO: Copied etree.so for ' + parch, level=xbmc.LOGDEBUG)
except Exception, e:
    xbmc.log('AUDO: Error Copying etree.so for ' + parch, level=xbmc.LOGERROR)
    xbmc.log(str(e), level=xbmc.LOGERROR)

try:
    if xbmcvfs.exists(p_constant_time):
        xbmcvfs.delete(p_constant_time)
    f_constant_time = xbmc.translatePath(__dependencies__ + '/lib/multiarch/_constant_time.so.' + parch)
    xbmcvfs.copy(f_constant_time, p_constant_time)
    xbmc.log('AUDO: Copied _constant_time.so for ' + parch, level=xbmc.LOGDEBUG)
except Exception, e:
    xbmc.log('AUDO: Error Copying _constant_time.so for ' + parch, level=xbmc.LOGERROR)
    xbmc.log(str(e), level=xbmc.LOGERROR)

try:
    if xbmcvfs.exists(p_openssl):
        xbmcvfs.delete(p_openssl)
    f_openssl = xbmc.translatePath(__dependencies__ + '/lib/multiarch/_openssl.so.' + parch)
    xbmcvfs.copy(f_openssl, p_openssl)
    xbmc.log('AUDO: Copied _openssl.so for ' + parch, level=xbmc.LOGDEBUG)
except Exception, e:
    xbmc.log('AUDO: Error Copying _openssl.so for ' + parch, level=xbmc.LOGERROR)
    xbmc.log(str(e), level=xbmc.LOGERROR)

try:
    if xbmcvfs.exists(p_padding):
        xbmcvfs.delete(p_padding)
    f_padding = xbmc.translatePath(__dependencies__ + '/lib/multiarch/_padding.so.' + parch)
    xbmcvfs.copy(f_padding, p_padding)
    xbmc.log('AUDO: Copied _padding.so for ' + parch, level=xbmc.LOGDEBUG)
except Exception, e:
    xbmc.log('AUDO: Error Copying _padding.so for ' + parch, level=xbmc.LOGERROR)
    xbmc.log(str(e), level=xbmc.LOGERROR)

try:
    if xbmcvfs.exists(plibcrypto):
        xbmcvfs.delete(plibcrypto)
    flibcrypto = xbmc.translatePath(__dependencies__ + '/lib/multiarch/libcrypto.so.1.0.0.' + parch)
    xbmcvfs.copy(flibcrypto, plibcrypto)
    os.symlink(plibcrypto, plibcryptolk)
    xbmc.log('AUDO: Copied libcrypto for ' + parch, level=xbmc.LOGDEBUG)
except Exception, e:
    xbmc.log('AUDO: Error Copying libcrypto for ' + parch, level=xbmc.LOGERROR)
    xbmc.log(str(e), level=xbmc.LOGERROR)

try:
    if xbmcvfs.exists(plibssl):
        xbmcvfs.delete(plibssl)
    flibssl = xbmc.translatePath(__dependencies__ + '/lib/multiarch/libssl.so.1.0.0.' + parch)
    xbmcvfs.copy(flibssl, plibssl)
    os.symlink(plibssl, plibssllk)
    xbmc.log('AUDO: Copied libssl for ' + parch, level=xbmc.LOGDEBUG)
except Exception, e:
    xbmc.log('AUDO: Error Copying libssl for ' + parch, level=xbmc.LOGERROR)
    xbmc.log(str(e), level=xbmc.LOGERROR)

try:
    if xbmcvfs.exists(plibffi):
        xbmcvfs.delete(plibffi)
    flibffi = xbmc.translatePath(__dependencies__ + '/lib/multiarch/libffi.so.6.0.4.' + parch)
    xbmcvfs.copy(flibffi, plibffi)
    os.symlink(plibffi, plibffilk)
    xbmc.log('AUDO: Copied libffi for ' + parch, level=xbmc.LOGDEBUG)
except Exception, e:
    xbmc.log('AUDO: Error Copying libffi for ' + parch, level=xbmc.LOGERROR)
    xbmc.log(str(e), level=xbmc.LOGERROR)

try:
    if xbmcvfs.exists(p_cffi_backend):
        xbmcvfs.delete(p_cffi_backend)
    f_cffi_backend = xbmc.translatePath(__dependencies__ + '/lib/multiarch/_cffi_backend.so.' + parch)
    xbmcvfs.copy(f_cffi_backend, p_cffi_backend)
    xbmc.log('AUDO: Copied _cffi_backend.so for ' + parch, level=xbmc.LOGDEBUG)
except Exception, e:
    xbmc.log('AUDO: Error Copying _cffi_backend.so for ' + parch, level=xbmc.LOGERROR)
    xbmc.log(str(e), level=xbmc.LOGERROR)

try:
    if xbmcvfs.exists(pyenc):
        xbmcvfs.delete(pyenc)
    fyenc = xbmc.translatePath(__dependencies__ + '/lib/multiarch/_yenc.so.' + parch)
    xbmcvfs.copy(fyenc, pyenc)
    xbmc.log('AUDO: Copied _yenc.so for ' + parch, level=xbmc.LOGDEBUG)
except Exception, e:
    xbmc.log('AUDO: Error Copying _yenc.so for ' + parch, level=xbmc.LOGERROR)
    xbmc.log(str(e), level=xbmc.LOGERROR)

try:
    if xbmcvfs.exists(psabyenc):
        xbmcvfs.delete(psabyenc)
    fsabyenc = xbmc.translatePath(__dependencies__ + '/lib/multiarch/sabyenc.so.' + parch)
    xbmcvfs.copy(fsabyenc, psabyenc)
    xbmc.log('AUDO: Copied sabyenc.so for ' + parch, level=xbmc.LOGDEBUG)
except Exception, e:
    xbmc.log('AUDO: Error Copying sabyenc.so for ' + parch, level=xbmc.LOGERROR)
    xbmc.log(str(e), level=xbmc.LOGERROR)

try:
    if parch != 'armv6l':
        if xbmcvfs.exists(plibgomp):
            xbmcvfs.delete(plibgomp)
        flibgomp = xbmc.translatePath(__dependencies__ + '/lib/multiarch/libgomp.so.1.' + parch)
        xbmcvfs.copy(flibgomp, plibgomp)
        xbmc.log('AUDO: Copied libgomp.so.1 for ' + parch, level=xbmc.LOGDEBUG)
except Exception, e:
    xbmc.log('AUDO: Error Copying libgomp.so.1 for ' + parch, level=xbmc.LOGERROR)
    xbmc.log(str(e), level=xbmc.LOGERROR)

try:
    if xbmcvfs.exists(ppar2):
        xbmcvfs.delete(ppar2)
    fpar2 = xbmc.translatePath(__dependencies__ + '/lib/multiarch/par2.' + parch)
    xbmcvfs.copy(fpar2, ppar2)
    os.chmod(ppar2, 0755)
    xbmc.log('AUDO: Copied par2 for ' + parch, level=xbmc.LOGDEBUG)
except Exception, e:
    xbmc.log('AUDO: Error Copying par2 for ' + parch, level=xbmc.LOGERROR)
    xbmc.log(str(e), level=xbmc.LOGERROR)

try:
    if xbmcvfs.exists(punrar):
        xbmcvfs.delete(punrar)
    funrar = xbmc.translatePath(__dependencies__ + '/lib/multiarch/unrar.' + parch)
    xbmcvfs.copy(funrar, punrar)
    os.chmod(punrar, 0755)
    xbmc.log('AUDO: Copied unrar for ' + parch, level=xbmc.LOGDEBUG)
except Exception, e:
    xbmc.log('AUDO: Error Copying unrar for ' + parch, level=xbmc.LOGERROR)
    xbmc.log(str(e), level=xbmc.LOGERROR)

try:
    if xbmcvfs.exists(p7za):
        xbmcvfs.delete(p7za)
    f7za = xbmc.translatePath(__dependencies__ + '/lib/multiarch/7za.' + parch)
    xbmcvfs.copy(f7za, p7za)
    os.chmod(p7za, 0755)
    xbmc.log('AUDO: Copied 7za for ' + parch, level=xbmc.LOGDEBUG)
except Exception, e:
    xbmc.log('AUDO: Error Copying 7za for ' + parch, level=xbmc.LOGERROR)
    xbmc.log(str(e), level=xbmc.LOGERROR)

xbmcvfs.File(xbmc.translatePath(__dependencies__ + '/arch.' + parch), 'w').close()
