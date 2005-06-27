#
# Conditional builds:
%bcond_without mapping	# build without support for schema mapping/rfc2307bis
#
Summary:	LDAP Name Service Switch Module
Summary(es):	Biblioteca NSS para LDAP
Summary(pl):	Modu³ NSS LDAP
Summary(pt_BR):	Biblioteca NSS para LDAP
Name:		nss_ldap
Version:	239
Release:	1
License:	LGPL
Group:		Base
Source0:	http://www.padl.com/download/%{name}-%{version}.tar.gz
# Source0-md5:	e30e3a3035e75933cd1a0acdeded1394
Patch0:		%{name}-am_fixes.patch
Patch1:		%{name}-nolibs.patch
Patch2:		%{name}-gecos-optional.patch
URL:		http://www.padl.com/nss_ldap.html
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_mapping:BuildRequires:	db-devel}
BuildRequires:	openldap-devel >= 2.0.0
BuildRequires:	cyrus-sasl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libdir		/%{_lib}

%description
nss_ldap is a C library extension (NSS module) which allows X.500 and
LDAP directory servers to be used as a primary source of aliases,
ethers, groups, hosts, networks, protocols, users, RPCs, services and
shadow passwords (instead of or in addition to using flat files or
NIS).

%description -l es
Este paquete contiene dos clientes de acceso a LDAP: nss_ldap y
pam_ldap.

nss_ldap son una serie de extensiones para la biblioteca C que
permiten que directorios X.500 y LDAP se usen como fuente de alias,
grupos, máquinas, protocolos, usuarios, RPCs, etc. (en vez de, o en
añadidura a, archivos normales o NIS)

pam_ldap es un módulo para Linux-PAM que da soporte al intercambio de
señas, clientes V2, Netscape SSL, ypldapd, políticas de contraseñas
Netscape Directory Server, autorización de acceso, hashes codificados,
etc.

%description -l pl
To jest nss_ldap - modu³ serwisu nazw odczytuj±cy dane z LDAP, który
mo¿na u¿ywaæ z glibc. Pozwala na korzystanie z serwerów X.500 i LDAP
jako g³ównego ¼ród³a aliasów, grup, hostów, sieci, protoko³ów,
u¿ytkowników, RPC, us³ug i hase³ (zamiast lub oprócz zwyk³ych plików
lub NIS).

%description -l pt_BR
Esse pacote contém dois clientes de acesso a LDAP: nss_ldap e
pam_ldap.

nss_ldap é uma série de extensões para a biblioteca C que permitem que
diretórios X.500 e LDAP sejam usados como fonte de apelidos, grupos,
máquinas, protocolos, usuários, RPCs, etc. (ao invés de, ou em adição
a, arquivos normais ou NIS)

pam_ldap é um módulo para o Linux-PAM que dá suporte a troca de
senhas, clientes V2, Netscape SSL, ypldapd, políticas de senhas
Netscape Directory Server, autorização de acesso, hashes encriptados,
etc.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-ldap-lib=openldap \
%if %{with mapping}
	--enable-schema-mapping \
	--enable-rfc2307bis \
%endif
	--enable-paged-results \
	--enable-configurable-krb5-ccname-env

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_libdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ANNOUNCE AUTHORS ChangeLog NEWS README nsswitch* ldap.conf
%attr(755,root,root) %{_libdir}/*.so*
%{_mandir}/man5/*
