%global tl_name turabian-formatting
%global tl_revision 58561

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Formatting based on Turabians Manual
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/turabian-formatting
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/turabian-formatting.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/turabian-formatting.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The turabian-formatting package provides Chicago-style formatting based
on Kate L. Turabian's "A Manual for Writers of Research Papers, Theses,
and Dissertations: Chicago Style for Students and Researchers" (9th
edition).

