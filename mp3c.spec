Summary: 	MP3 creator for audiocds with usage of CDDB
Name: 		mp3c
Version: 	0.31
Release: 	%mkrel 8
License: 	GPL
Group: 		Sound
URL:		http://wspse.de/WSPse/Linux-MP3c.php3
Source: 	ftp://ftp.wspse.de/pub/linux/wspse/%{name}-%{version}.tar.bz2
BuildRequires:  ncurses-devel
BuildRoot: 	%{_tmppath}/%{name}-%{version}-buildroot

%description
This program reads the TOC from audio CDs, gets the CDDB entry for it, 
and converts the audio tracks to mp3 or Ogg Vorbis format.
(under usage of any CD grabber and encoder).

It has a comfortable text-based UI, but you can also create a shell script for 
automated processing of a CD.

The default settings require oggenc from the vorbis-tools package and 
cdparanoia.


%prep

%setup -q

%build

%configure2_5x \
    --with-cddb-path=%{_datadir}/apps/kscd/cddb \
    --enable-oggdefaults

%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall

%{find_lang} %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS BATCH.README BUGS CDDB_HOWTO ChangeLog FAQ NEWS OTHERS 
%doc README patches/cdparanoia.diff patches/encoder.diff TODO
%{_bindir}/mp3c
%{_mandir}/man1/mp3c.1*


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.31-8mdv2011.0
+ Revision: 620400
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.31-7mdv2010.0
+ Revision: 430097
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 0.31-6mdv2009.0
+ Revision: 252926
- rebuild

* Fri Mar 07 2008 Oden Eriksson <oeriksson@mandriva.com> 0.31-4mdv2008.1
+ Revision: 181395
- rebuild
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Sep 09 2007 Oden Eriksson <oeriksson@mandriva.com> 0.31-2mdv2008.0
+ Revision: 83808
- rebuild


* Mon Jul 31 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.31-1mdv2007.0
- New release 0.31

* Wed Mar 08 2006 Götz Waschk <waschk@mandriva.org> 0.30-1mdk
- new version

* Wed Jul 06 2005 Lenny Cartier <lenny@mandriva.com> 0.29-2mdk
- rebuild

* Sat Jun 26 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.29-1mdk
- 0.29

* Thu Jun 03 2004 Michael Scherer <misc@mandrake.org> 0.28-2mdk 
- rebuild for new libintl
- BuildRequires

* Fri Apr 16 2004 Götz Waschk <waschk@linux-mandrake.com> 0.28-1mdk
- fix url
- enable Ogg as default
- drop patch
- new version

