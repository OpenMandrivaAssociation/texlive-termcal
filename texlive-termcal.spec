# revision 22514
# category Package
# catalog-ctan /macros/latex/contrib/termcal
# catalog-date 2011-05-17 01:53:44 +0200
# catalog-license lppl1
# catalog-version 1.8
Name:		texlive-termcal
Version:	1.8
Release:	7
Summary:	Print a class calendar
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/termcal
License:	LPPL1
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/termcal.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/termcal.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/termcal.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package is intended to print a term calendar for use in
planning a class. It has a flexible mechanism for specifying
which days of the week are to be included and for inserting
text either regularly on the same day each week, or on selected
days, or for a series of consecutive days. It also has a
flexible mechanism for specifing class and nonclass days. Text
may be inserted into consecutive days so that it automatically
flows around nonclass days.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.8-2
+ Revision: 756589
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.8-1
+ Revision: 719669
- texlive-termcal
- texlive-termcal
- texlive-termcal

