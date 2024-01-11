class Vce < Formula
  desc "Randroid's Text to Voice Script. Using OpenAI's API."
  homepage "https://github.com/randroid88/homebrew-vce"
  url "https://github.com/randroid88/homebrew-vce/archive/refs/tags/1.0.1.tar.gz"
  sha256 "dc12c909b9726dbfac883911a6d045ac75c0fa470541c3f3220db9862efab61d"

  def install
    libexec.install Dir["*.py"]
    bin.install "vce.py" => "vce"
    chmod 0555, bin/"vce"
  end

  test do
    system "#{bin}/vce"
  end
end