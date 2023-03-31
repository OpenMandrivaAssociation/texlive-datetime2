Name:		texlive-datetime2
Version:	63102
Release:	2
Summary:	Formats for dates, times and time zones
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/datetime2
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/datetime2.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/datetime2.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/datetime2.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides commands for formatting dates, times and
time zones and redefines \today to use the same formatting
style. In addition to \today, you can also use \DTMcurrenttime
(current time) or \DTMnow (current date and time). Dates and
times can be saved for later use. The accompanying
datetime2-calc package can be used to convert date-times to
UTC+00:00. Language and regional support is provided by
independently maintained and installed modules. The
datetime2-calc package uses the pgfcalendar package (part of
the PGF/TikZ bundle). This package replaces datetime.sty which
is now obsolete.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/datetime2
%{_texmfdistdir}/tex/latex/datetime2
%doc %{_texmfdistdir}/doc/latex/datetime2

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
