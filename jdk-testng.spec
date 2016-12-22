Name     : jdk-testng
Version  : 1
Release  : 1
URL      : http://repo.maven.apache.org/maven2/org/testng/testng/5.10/testng-5.10-jdk15.jar
Source0  : http://repo.maven.apache.org/maven2/org/testng/testng/5.10/testng-5.10-jdk15.jar
Source1  : http://repo.maven.apache.org/maven2/org/testng/testng/5.10/testng-5.10.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
BuildRequires : javapackages-tools
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six

%description
No detailed description available

%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java

mv %{SOURCE0} %{buildroot}/usr/share/java/testng-jdk15.jar
mv %{SOURCE1} %{buildroot}/usr/share/maven-poms/testng.pom

# Creates metadata
python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/testng.xml \
%{buildroot}/usr/share/maven-poms/testng.pom \
%{buildroot}/usr/share/java/testng-jdk15.jar \

%files
%defattr(-,root,root,-)
/usr/share/maven-metadata/testng.xml
/usr/share/maven-poms/testng.pom
/usr/share/java/testng-jdk15.jar
