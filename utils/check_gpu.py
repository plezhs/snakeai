import subprocess
import sys
import platform
import re

# PyTorch 버전 → CUDA 버전 → index-url 매핑
CUDA_INDEX_MAP = {
    "12.1": "https://download.pytorch.org/whl/cu121",
    "12.0": "https://download.pytorch.org/whl/cu120",
    "11.8": "https://download.pytorch.org/whl/cu118",
    "11.7": "https://download.pytorch.org/whl/cu117",
    "11.6": "https://download.pytorch.org/whl/cu116",
}

def get_cuda_version():
    try:
        output = subprocess.check_output("nvidia-smi", stderr=subprocess.DEVNULL)
        text = output.decode()
        match = re.search(r"CUDA Version: (\d+\.\d+)", text)
        if match:
            return match.group(1)
    except Exception:
        pass
    return None

def choose_cuda_index_url(cuda_version):
    for version, url in CUDA_INDEX_MAP.items():
        if cuda_version.startswith(version):
            return url
    return None  # 지원하지 않는 버전일 경우

def install_torch(cuda_version=None):
    pip_cmd = [sys.executable, "-m", "pip", "install"]

    if cuda_version:
        index_url = choose_cuda_index_url(cuda_version)
        if index_url:
            print(f"✅ CUDA {cuda_version} 버전에 맞는 PyTorch를 설치합니다.")
            torch_cmd = pip_cmd + [
                "torch", "torchvision", "torchaudio",
                "--index-url", index_url
            ]
        else:
            print(f"⚠️ CUDA {cuda_version}는 자동 지원되지 않아 CPU 버전으로 설치합니다.")
            torch_cmd = pip_cmd + ["torch", "torchvision", "torchaudio"]
    else:
        print("⚠️ NVIDIA GPU가 감지되지 않았습니다. CPU 버전 PyTorch를 설치합니다.")
        torch_cmd = pip_cmd + ["torch", "torchvision", "torchaudio"]

    try:
        print("🔧 PyTorch 설치 중...")
        subprocess.check_call(torch_cmd)
        print("✅ PyTorch 설치가 완료되었습니다.")
    except subprocess.CalledProcessError:
        print("❌ PyTorch 설치 중 오류 발생.")
        sys.exit(1)

def main():
    print("🚀 시스템 환경 확인 중...")
    print(f"OS: {platform.system()} {platform.release()}")
    print(f"Python 버전: {platform.python_version()}")

    cuda_version = get_cuda_version()
    install_torch(cuda_version)

if __name__ == "__main__":
    main()
