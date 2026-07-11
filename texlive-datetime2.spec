%global tl_name datetime2
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.5.7
Release:	%{tl_revision}.1
Summary:	Formats for dates, times and time zones
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/datetime2
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/datetime2.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/datetime2.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/datetime2.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(etoolbox)
Requires:	texlive(tracklang)
Requires:	texlive(xkeyval)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides commands for formatting dates, times and time
zones and redefines \today to use the same formatting style. In addition
to \today, you can also use \DTMcurrenttime (current time) or \DTMnow
(current date and time). Dates and times can be saved for later use. The
accompanying datetime2-calc package can be used to convert date-times to
UTC+00:00. Language and regional support is provided by independently
maintained and installed modules. The datetime2-calc package uses the
pgfcalendar package (part of the PGF/TikZ bundle). This package replaces
datetime.sty which is now obsolete.

