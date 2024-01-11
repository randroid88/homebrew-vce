class Vce < Formula
  desc "Randroid's Text to Voice Script. Using OpenAI's API."
  homepage "https://github.com/randroid88/homebrew-vce"
  url "https://github.com/randroid88/homebrew-vce/archive/refs/tags/v1.0.0.tar.gz"
  sha256 ""

  def install
    bin.install "vce.py" => "vce"
    chmod 0555, bin/"vce"
  end

  test do
    system "#{bin}/vce"
  end
end