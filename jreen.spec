
Name:    jreen
Summary: Qt XMPP Library
Version: 1.0.5
Release: 1%{?dist}
 
License: GPLv2+
URL:     http://qutim.org/jreen
#URL:     https://github.com/euroelessar/jreen
%if 0%{?snap}
# git clone git://github.com/euroelessar/jreen.git ; cd jreen
# git archive --prefix=jreen-1.0.1/ v1.0.1 | xz > ../jreen-1.0.1.tar.xz
#Source0: jreen-%{version}.tar.xz
%else
Source0: http://qutim.org/dwnl/33/libjreen-%{version}.tar.bz2
%endif

## upstream patches

BuildRequires: cmake
BuildRequires: pkgconfig(libidn)
BuildRequires: pkgconfig(qca2)
BuildRequires: pkgconfig(qjdns)
BuildRequires: pkgconfig(QtNetwork) 
BuildRequires: zlib-devel

Requires: qca-ossl%{?_isa}

%description
%{summary}.
 
%package devel
Summary:  Development files for %{name} 
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.
 
 
%prep
%setup -q -n libjreen-%{version}

# nuke bundled libs out of paranoia -- rex
rm -rfv 3rdparty/*


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake} \
  -DJREEN_USE_SYSTEM_JDNS:BOOL=ON \
  ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%check
export PKG_CONFIG_PATH=%{buildroot}%{_datadir}/pkgconfig:%{buildroot}%{_libdir}/pkgconfig
test "$(pkg-config --modversion libjreen)" = "%{version}"

 
%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
 
%files 
%doc AUTHORS ChangeLog COPYING README
%{_libdir}/libjreen.so.1*
 
%files devel
%{_includedir}/jreen/
%{_libdir}/libjreen.so
%{_libdir}/pkgconfig/libjreen.pc
 

%changelog
* Sun Apr 01 2012 Rex Dieter <rdieter@fedoraproject.org> 1.0.5-1
- jreen-1.0.5 (#807634)

* Wed Mar 28 2012 Rex Dieter <rdieter@fedoraproject.org> 1.0.4-1
- jreen-1.0.4 (#807634)

* Sat Jan 07 2012 Rex Dieter <rdieter@fedoraproject.org> 1.0.1-4
- upstream gcc47 patch

* Sat Jan 07 2012 Rex Dieter <rdieter@fedoraproject.org> 1.0.1-3
- update URL, Source0

* Fri Jan 06 2012 Rex Dieter <rdieter@fedoraproject.org> 1.0.1-2
- fix URL
- Requires: qca-ossl
- delete bundled libs

* Fri Jan 06 2012 Rex Dieter <rdieter@fedoraproject.org> 1.0.1-1
- 1.0.1
- -DJREEN_USE_SYSTEM_JDNS:BOOL=ON

* Mon Nov 14 2011 Rex Dieter <rdieter@fedoraproject.org> 0.1.0-0.4.20110901
- pkgconfig-style deps

* Thu Sep 01 2011 Rex Dieter <rdieter@fedoraproject.org> 0.1.0-0.3.20110901
- 20110901 snapshot

* Tue Aug 16 2011 Rex Dieter <rdieter@fedoraproject.org> 0.1.0-0.2.20110816
- 20110816 snapshot

* Thu Jun 02 2011 Rex Dieter <rdieter@fedoraproject.org> 0.1.0-0.1.20010602
- first try, 0.1.0 20010602 git snapshot

