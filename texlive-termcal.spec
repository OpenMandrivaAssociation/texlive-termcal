# revision 22514
# category Package
# catalog-ctan /macros/latex/contrib/termcal
# catalog-date 2011-05-17 01:53:44 +0200
# catalog-license lppl1
# catalog-version 1.8
Name:		texlive-termcal
Version:	1.8
Release:	1
Summary:	Print a class calendar
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/termcal
License:	LPPL1
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/termcal.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/termcal.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/termcal.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This package is intended to print a term calendar for use in
planning a class. It has a flexible mechanism for specifying
which days of the week are to be included and for inserting
text either regularly on the same day each week, or on selected
days, or for a series of consecutive days. It also has a
flexible mechanism for specifing class and nonclass days. Text
may be inserted into consecutive days so that it automatically
flows around nonclass days.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/termcal/termcal.sty
%doc %{_texmfdistdir}/doc/latex/termcal/Contents
%doc %{_texmfdistdir}/doc/latex/termcal/README
%doc %{_texmfdistdir}/doc/latex/termcal/termcal.pdf
#- source
%doc %{_texmfdistdir}/source/latex/termcal/termcal.dtx
%doc %{_texmfdistdir}/source/latex/termcal/termcal.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
