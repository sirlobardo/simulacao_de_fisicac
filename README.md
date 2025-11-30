# 📌 Simulação de Física — Trajetória de Partícula Carregada

Uma partícula com **carga `q`** e **massa `m`**, com **velocidade inicial na direção vertical**, entra em uma região com **campo elétrico constante na direção horizontal**, no ponto  
**A = (x0, y0)** no instante **t0**.

Após um intervalo de tempo `Δt = t - t0`, o campo elétrico passa a **girar com velocidade angular constante `ω`**.

**🎯 Objetivo:** construir a trajetória da partícula no plano `(x, y)` para tempos `t > t0`.

---
# 📘 Modelo Físico

A única força atuante é a **força elétrica**:

$$
\vec{F}(t) = q \cdot \vec{E}(t)
$$

Pela **2ª Lei de Newton**:

$$
m\cdot \vec{a}(t) = q\cdot \vec{E}(t)
\quad\Rightarrow\quad
\vec{a}(t) = \frac{q}{m}\vec{E}(t)
$$

---

## 📡 Campo Elétrico Adotado

$$
\vec{E}(t) = (E, 0) \quad t \le t_0
$$

$$
\vec{E}(t) = (E\cos[\omega(t - t_0)],\ E\sin[\omega(t - t_0)]),\quad t > t_0
$$

---

## 🧮 Equações da Trajetória (usadas na simulação)

$$
x(t) = v_{x1}t + \frac{qE}{2m\omega^2}\left(1 - \cos(\omega t)\right)
$$

$$
y(t) = y_1 + v_{y1}t + \frac{qE}{2m\omega^2}\left(t - \frac{\sin(\omega t)}{\omega}\right)
$$

Essas equações foram obtidas pela **integração analítica** da aceleração:

1. Integração da aceleração → velocidade  
2. Nova integração → posição

---

## 📊 Parâmetros Utilizados


| Parâmetro | Valor (texto) | Descrição |
|---|---:|---|
| q | `1.6e-19 C` | carga do elétron |
| m | `9.11e-31 kg` | massa do elétron |
| E | `3e5 V/m` | módulo do campo elétrico |
| v_x0 | `2e6 m/s` | velocidade inicial em x (em t0) |
| v_y0 | `0 m/s` | velocidade inicial em y (em t0) |
| omega | `2e7 rad/s` | frequência angular |
| t0 | `0.1 us` | instante de comutação (início da rotação) |

---

## 🖥️ Requisitos

### Instale o Python
https://www.python.org/downloads/

### Instale os pacotes necessários
```bash
pip install numpy
pip install matplotlib
```

---

## ▶️ Executando a simulação

Rodar o script:
```bash
python main.py
```

Os parâmetros (`q`, `m`, `x0`, `y0`, `vy0`, `E`, `t0`, `omega`) devem ser alterados dentro do arquivo.

---

## 📷 Resultado da Simulação

![Plot padrão](imagens/4.png) |

---
