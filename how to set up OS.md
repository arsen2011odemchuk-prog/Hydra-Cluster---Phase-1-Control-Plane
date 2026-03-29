# 🧠 Hydra Cluster Phase 1: Master Node Software Foundation

This repository contains the "Zero-Touch" automation logic and architectural foundation for **Node 1** of the Hydra AI Cluster. This node serves as the **Control Plane** (The Brain), responsible for resource orchestration, workload scheduling, and managing the distributed neural network tasks across the remaining three nodes.

---

## ## 🚀 Overview: What This Code Accomplishes

The `setup.sh` script is a professional-grade deployment tool designed to transform a standard Ubuntu 24.04 LTS headless installation into a hardened AI orchestration hub.

### 1. Automation (Zero-Touch Deployment)
Manual configuration of a Kubernetes environment involves over 50 complex commands and significant risk of human error. This script automates the entire pipeline—from repository injection to firewall hardening—ensuring a consistent "Source of Truth" for your cluster's OS.

### 2. Containerization (Docker Engine)
Docker provides the "Standard Unit of Software" for AI. By utilizing Docker:
* **Isolation:** AI models (like Llama 3 or Stable Diffusion) run in isolated environments, preventing library conflicts.
* **Portability:** You can pull pre-baked AI images from Hugging Face or Docker Hub and run them instantly without manual Python environment setup.

### 3. Orchestration (K3s Lightweight Kubernetes)
K3s is a highly optimized, CNCF-certified Kubernetes distribution. In this 4-node project, K3s acts as the cluster's operating system:
* **Self-Healing:** If a worker node fails, K3s automatically redistributes the AI inference task to a healthy node.
* **Scalability:** It treats all 4 CPUs and all future GPUs as a single pool of resources.

### 4. GPU Future-Proofing (NVIDIA Container Toolkit)
While the initial setup uses an NVIDIA GT 210, this script installs the modern **NVIDIA Container Toolkit**. This creates a software "bridge" that allows Docker and K3s to communicate with GPU hardware. When you upgrade to a modern RTX card, the cluster will recognize the CUDA cores immediately without needing a software rebuild.

---

## 🛠️ Detailed Step-by-Step Setup Guide

### Phase A: Hardware & OS Prep
1. Install **Ubuntu Server 24.04 LTS** (64-bit) on your AMD Ryzen 3 4100 system.
2. Ensure the system is connected via **Ethernet** (WiFi is not recommended for cluster stability).
3. Identify the local IP address of the machine via your router or by typing `hostname -I`.

### Phase B: Remote Deployment
From your main workstation/laptop, perform the following:

1. **Access the Node:**
   ```bash
   ssh username@<your-node-ip>
