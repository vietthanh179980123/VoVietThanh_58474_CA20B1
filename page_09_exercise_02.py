"""
Author: Võ Viết Thanh
Date: 28/08/2021
Program: What does the central processing unit (CPU) do
Solution:
    1. Fetch

    First, the CPU fetches instructions from program memory. Program memory is the location of the instruction.

    This location also stores a number that is the address of the next instruction that needs to be fetched.

    The program counter increases itself by the duration of the instruction after the instruction is fetched so that it can include the address of the next instruction in the sequence.

    2. Decode

    After the CPU can decide what to do next with the data, this step is the decoding stage.

    This phase is done by the circuit known as the Instruction Decoder. The instruction then transforms into signals that monitor other parts of the CPU.

    Instruction Set Architecture (ISA) for the CPU defines how the instruction will be interpreted.

    3. Execute

    The execution stage takes place after the steps of fetching and decoding.

    This stage can consist of a single or a series of actions, depending on the CPU architecture.

    Throughout each action, various parts of the CPU are connected electrically, so that they can execute the desired activity.

    The results of the execution are then updated to the internal CPU register
    ....
"""
