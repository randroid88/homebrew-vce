class Vce < Formula
  desc "Randroid's Text to Voice Script. Using OpenAI's API."
  homepage "https://github.com/randroid88/homebrew-vce"
  url "https://github.com/randroid88/homebrew-vce/archive/refs/tags/1.0.0.tar.gz"
  sha256 "6f3373152c8e4e98a02a4bd9eec947fb5891209e7c0dcce40d564dfd720d628c"

  def install
    libexec.install Dir["*.py"]
    bin.install "vce.py" => "vce"
    chmod 0555, bin/"vce"
  end

  test do
    system "#{bin}/vce"
  end
end