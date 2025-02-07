# Usar a imagem oficial do Python 3.12
FROM python:3.12-bookworm

# Evitar perguntas durante a instalação de pacotes
ENV DEBIAN_FRONTEND=noninteractive

# Instalar dependências do sistema
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Atualizar pip
RUN python -m pip install --upgrade pip

# Criar usuário não-root
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && mkdir -p /workspace \
    && chown ${USERNAME}:${USERNAME} /workspace

USER $USERNAME
# Adicionar .local/bin ao PATH do usuário
ENV PATH="/home/vscode/.local/bin:${PATH}"
WORKDIR /workspace
