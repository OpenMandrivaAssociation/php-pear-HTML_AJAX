%define     _class      HTML
%define     _subclass   AJAX
%define     upstream_name   %{_class}_%{_subclass}

Name:       php-pear-%{upstream_name}
Version:    0.5.6
Release:    9
Summary:    PHP and JavaScript AJAX library
License:    LGPL
Group:      Development/PHP
URL:        https://pear.php.net/package/%{upstream_name}
Source0:    http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:   php-pear
BuildArch:  noarch
BuildRequires:  php-pear

%description
Provides PHP and JavaScript libraries for performing AJAX
(Communication from JavaScript to your browser without reloading the
page)

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/docs/*
%{_datadir}/pear/%{_class}
%{_datadir}/pear/data/%{upstream_name}
%{_datadir}/pear/packages/%{upstream_name}.xml



%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 0.5.6-7mdv2012.0
+ Revision: 741988
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 0.5.6-6
+ Revision: 679339
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.5.6-5mdv2011.0
+ Revision: 613666
- the mass rebuild of 2010.1 packages

* Sat Dec 12 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.5.6-4mdv2010.1
+ Revision: 477858
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 0.5.6-3mdv2010.0
+ Revision: 441110
- rebuild

* Mon Feb 16 2009 Jerome Martin <jmartin@mandriva.org> 0.5.6-2mdv2009.1
+ Revision: 341144
- import php-pear-HTML_AJAX


