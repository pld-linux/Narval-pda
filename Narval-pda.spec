%define short_name pda

Summary:	Personal Digital Asistant
Summary(pl):	Cyfrowy asystent osobisty
Name:		Narval-%{short_name}
Version:	20011016
Release:	1
Source0:	ftp://ftp.logilab.org/pub/narval/applications/%{short_name}-%{version}.npm
License:	GPL
Group:		Applications
Group(de):	Applikationen
Group(pl):	Aplikacje
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	Narval
Url:		http://www.logilab.org/narval/app.html

%description
The PDA recipe is an example of how Narval can be used as a simple web
server to manage your agenda and contact lists. It also shows some of
Narval introspection features, with recipes showing available recipes,
actions and transformations, as well as how to instanciate a new plan
from with a recipe.

%description -l pl
Recepta PDA to przyk³±d jak NArval mo¿e byæ wykorzystany jako prosty
werwer WWW do zarz±dzania twoim czasem i list± kontaktów.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_datadir}/narval/apps
install %{SOURCE0} $RPM_BUILD_ROOT/%{_datadir}/narval/apps

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/narval/apps/*
