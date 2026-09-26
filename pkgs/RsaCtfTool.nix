{ buildPythonPackage, fetchFromGitHub }:
(buildPythonPackage {
  pname = "RsaCtfTool";
  version = "1.0.0";
  format = "setuptools";
  src = fetchFromGitHub {
    owner = "RsaCtfTool";
    repo = "RsaCtfTool";
    rev = "master";
    sha256 = "sha256-x4B+oDcyuWddDvXXw0hjr0CaQCbystlVPGGDpkhgryY=";
  };
})
