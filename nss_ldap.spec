# $Revision: 1.32 $Date: 2001-07-04 13:48:35 $
#
# Conditional builds:	
# --with openldap1 - build with openldap < 2.0.0
#
Summary:	LDAP Name Service Switch Module
Name:		nss_ldap
Version:	159
Release:	1
License:	LGPL
Group:		Base
Group(de):	Gründsätzlich
Group(pl):	Podstawowe
Source0:	ftp://ftp.padl.com/pub/%{name}-%{version}.tar.gz
Patch0:		%{name}-am_fixes.patch
URL:		http://www.padl.com/nss_ldap.html
BuildRequires:	autoconf
BuildRequires:	automake
%{!?_with_openldap1:BuildRequires: openldap-devel >= 2.0.0}
%{?_with_openldap1:BuildRequires:  openldap-devel <  2.0.0}
%{?_with_openldap1:BuildRequires:  openldap-devel >  1.2.0}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libdir		/lib

%description 
This is nss_ldap, a name service switch module that can be used with
glibc-2.1.xx.

%prep
%setup -q
%patch -p1

%build
rm -f missing
aclocal
autoconf
automake -a -c
%configure \
	--with-ldap-lib=openldap
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__install} -d $RPM_BUILD_ROOT{/etc,%{_libdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf ANNOUNCE AUTHORS ChangeLog NEWS README nsswitch* doc/rfc*

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc/*.gz
%attr(0755,root,root) %{_libdir}/*.so
