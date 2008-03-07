Summary: 	MP3 creator for audiocds with usage of CDDB
Name: 		mp3c
Version: 	0.31
Release: 	%mkrel 3
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
