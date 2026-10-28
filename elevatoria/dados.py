"""Leitura do log SCADA da estação elevatória e preparação dos dados.

Este módulo é a porta de entrada da aplicação: transforma o texto do log em registros
estruturados e em séries numéricas. As funções marcadas com `NotImplementedError` são as
issues abertas do Marco 1; as docstrings descrevem o contrato que cada uma deve cumprir.
Não mude nomes nem assinaturas públicas: outros módulos e os testes dependem deles.
"""
from __future__ import annotations

import array
import re
import sys
from dataclasses import dataclass
from datetime import datetime
from typing import Callable

import numpy as np

from elevatoria.serie import SerieTemporal
from fornecido.cronometro import cronometrar


# ---------------------------------------------------------------------------------------
# Issue #1: leitor do log
# ---------------------------------------------------------------------------------------


LINHA = re.compile(
    r"""
    ^
    (?P<data>[0-9]{4}-[0-9]{2}-[0-9]{2})\s+
    (?P<hora>[0-9]{2}:[0-9]{2}:[0-9]{2})\s+
    (?P<nivel>[A-Z]+)\s+
    (?P<tag>[A-Z]{1,2}[0-9]{1,3})\s+
    (?P<resto>.+)
    $
    """,
    re.VERBOSE)


@dataclass(frozen=True)
class Registro:
    """Uma linha válida do log: instante, nível, tag e os pares chave=valor convertidos."""

    instante: datetime
    nivel: str
    tag: str
    valores: dict[str, float | str]


def valida_tag(s: str) -> bool:
    return bool(re.fullmatch(r"[A-Z]{1,2}[0-9]{1,3}",s))
    

def ler_log(texto: str) -> tuple[list[Registro], list[str]]:    
    registros = []
    invalidas = []

    for linha in texto.splitlines():
        if not linha.strip():
            continue
        match = LINHA.fullmatch(linha)
        if match:
            dados = match.groupdict()
            if valida_tag(dados["tag"]):
                valores = {}
                data_hora_str = f"{dados['data']} {dados['hora']}"
                instante_dt = datetime.strptime(data_hora_str, "%Y-%m-%d %H:%M:%S")
            
                for par in dados["resto"].split():
                    chave, valor_raw = par.split('=', 1)
                    try:
                        valor = float(valor_raw)
                    except ValueError:
                        valor = valor_raw
                    valores[chave] = valor    

                reg = Registro(
                    instante = instante_dt,
                    nivel = dados["nivel"],
                    tag = dados["tag"],
                    valores = valores
                )
                registros.append(reg)

            else:
                invalidas.append(linha)
        else:
            invalidas.append(linha)
            
    return registros, invalidas



    

def por_tag(registros: list[Registro], tag: str) -> list[Registro]:
    """Registros da `tag`, na ordem original."""
    return [r for r in registros if r.tag == tag]


def contagem_por_tag(registros: list[Registro]) -> dict[str, int]:
    tags = {}
    for r in registros:
        if r.tag in tags:
            tags[r.tag] += 1
        else:
            tags[r.tag] = 1
    return tags


def serie(registros: list[Registro], tag: str, chave: str) -> SerieTemporal:
    valores = []
    for i in registros:
        if i.tag == tag and chave in i.valores:
            valores.append(i.valores[chave])

    return SerieTemporal.de_lista(valores)
            

# ---------------------------------------------------------------------------------------
# Issue #2: conversores por tag
# ---------------------------------------------------------------------------------------
def criar_conversores(escalas: dict[str, float]) -> dict[str, Callable[[float], float]]:
    """Dado `{tag: fator}`, devolve `{tag: f}`, em que `f(c) = c * fator` da própria tag.

    Cada `f` é uma lambda. Cuidado com o *late binding*: cada função deve usar o fator da
    sua tag, e não o último fator do dicionário (veja a issue #2 no enunciado).
    """
    raise NotImplementedError("issue #2: criar_conversores")


# ---------------------------------------------------------------------------------------
# Issue #3: memória e tempo
# ---------------------------------------------------------------------------------------
def medir_memoria(contagens: np.ndarray) -> dict[str, int]:
    """Bytes ocupados pelas `contagens` (ndarray 1D de inteiros de 0 a 4095) em cada estrutura.

    Devolve um dicionário com exatamente estas chaves:

    - `"list"`: a lista `contagens.tolist()`; o total é `sys.getsizeof(lista)` mais a soma de
      `sys.getsizeof(x)` para cada elemento `x`;
    - `"array('H')"`: um `array.array("H", ...)`; conte só os dados (`itemsize * len`);
    - `"uint16"`, `"int32"`, `"int64"`, `"float32"`, `"float64"`: o `ndarray` convertido para
      esse `dtype`; conte só os dados (atributo `.nbytes`).

    Levanta `ValueError` se `contagens` não for um ndarray 1D de inteiros.
    """
    raise NotImplementedError("issue #3: medir_memoria")


def converter_laco(contagens: list[int]) -> list[float]:
    """Converte contagens em kPa (`c * 600 / 4095`) com `for` e `append`."""
    raise NotImplementedError("issue #3: converter_laco")


def converter_compreensao(contagens: list[int]) -> list[float]:
    """Converte contagens em kPa (`c * 600 / 4095`) com uma compreensão de lista."""
    raise NotImplementedError("issue #3: converter_compreensao")


def converter_map(contagens: list[int]) -> list[float]:
    """Converte contagens em kPa (`c * 600 / 4095`) com `map` e uma lambda."""
    raise NotImplementedError("issue #3: converter_map")


def converter_vetorizado(contagens: np.ndarray) -> np.ndarray:
    """Converte contagens em kPa (`c * 600 / 4095`) com uma operação vetorizada do NumPy."""
    raise NotImplementedError("issue #3: converter_vetorizado")


def medir_tempos(contagens: np.ndarray, k: int = 10) -> dict[str, float]:
    """Tempo médio (s) de cada versão da conversão, em `k` repetições.

    Use `cronometrar` (de `fornecido.cronometro`). Chaves: `"laço"`, `"compreensão"` e
    `"map+lambda"` (que recebem a lista `contagens.tolist()`, criada uma única vez, fora da
    medição) e `"vetorizado"` (que recebe o próprio `ndarray`).
    """
    raise NotImplementedError("issue #3: medir_tempos")
