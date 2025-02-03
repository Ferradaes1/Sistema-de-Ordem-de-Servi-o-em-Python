import tkinter as tk
from tkinter import messagebox
import sqlite3

class OrdemServicoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gerenciamento de Ordens de Serviço")
        self.root.geometry("700x500")
        self.root.config(bg="#f7f7f7")

        # Conexão com banco de dados SQLite
        self.conn = sqlite3.connect('ordens_servico.db')
        self.cursor = self.conn.cursor()
        self.create_table()

        # Widgets principais
        self.create_widgets()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS ordens_servico (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_cliente TEXT,
                descricao TEXT,
                data DATE
            )
        """)
        self.conn.commit()

    def create_widgets(self):
        # Frame principal
        main_frame = tk.Frame(self.root, bg="#f7f7f7")
        main_frame.pack(pady=20)

        # Título
        self.title_label = tk.Label(main_frame, text="Gerenciamento de Ordens de Serviço", font=("Helvetica", 18, "bold"), bg="#f7f7f7")
        self.title_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Campos de entrada
        self.nome_cliente_label = tk.Label(main_frame, text="Nome do Cliente", bg="#f7f7f7", font=("Helvetica", 12))
        self.nome_cliente_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.nome_cliente_entry = tk.Entry(main_frame, font=("Helvetica", 12), width=30)
        self.nome_cliente_entry.grid(row=1, column=1, padx=10, pady=10)

        self.descricao_label = tk.Label(main_frame, text="Descrição do Serviço", bg="#f7f7f7", font=("Helvetica", 12))
        self.descricao_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.descricao_entry = tk.Entry(main_frame, font=("Helvetica", 12), width=30)
        self.descricao_entry.grid(row=2, column=1, padx=10, pady=10)

        self.data_label = tk.Label(main_frame, text="Data da Ordem", bg="#f7f7f7", font=("Helvetica", 12))
        self.data_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.data_entry = tk.Entry(main_frame, font=("Helvetica", 12), width=30)
        self.data_entry.grid(row=3, column=1, padx=10, pady=10)

        # Botões
        self.add_button = tk.Button(main_frame, text="Adicionar Ordem", command=self.add_ordem, font=("Helvetica", 12), bg="#4CAF50", fg="white", relief="flat")
        self.add_button.grid(row=4, column=0, columnspan=2, pady=20)

        self.view_button = tk.Button(main_frame, text="Ver Ordens", command=self.view_ordens, font=("Helvetica", 12), bg="#2196F3", fg="white", relief="flat")
        self.view_button.grid(row=5, column=0, columnspan=2, pady=10)

    def add_ordem(self):
        nome_cliente = self.nome_cliente_entry.get()
        descricao = self.descricao_entry.get()
        data = self.data_entry.get()

        if nome_cliente and descricao and data:
            self.cursor.execute("""
                INSERT INTO ordens_servico (nome_cliente, descricao, data)
                VALUES (?, ?, ?)
            """, (nome_cliente, descricao, data))
            self.conn.commit()
            messagebox.showinfo("Sucesso", "Ordem de serviço adicionada com sucesso!")
            self.clear_entries()
            self.view_ordens()  # Atualiza a lista automaticamente
        else:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios.")

    def view_ordens(self):
        ordens_window = tk.Toplevel(self.root)
        ordens_window.title("Ordens de Serviço")
        ordens_window.geometry("700x400")
        ordens_window.config(bg="#f7f7f7")

        listbox_frame = tk.Frame(ordens_window, bg="#f7f7f7")
        listbox_frame.pack(pady=20)

        listbox = tk.Listbox(listbox_frame, width=80, height=10, font=("Helvetica", 12), selectmode=tk.SINGLE)
        listbox.pack()

        # Menu de contexto
        self.context_menu = tk.Menu(ordens_window, tearoff=0)
        self.context_menu.add_command(label="Editar", command=lambda: self.edit_ordem(listbox))
        self.context_menu.add_command(label="Excluir", command=lambda: self.delete_ordem(listbox))

        # Função para capturar o clique direito
        def show_context_menu(event):
            try:
                self.selected_ordem = listbox.curselection()[0]
                self.context_menu.post(event.x_root, event.y_root)
            except IndexError:
                return  # Se não houver seleção, não faz nada

        # Carrega as ordens do banco de dados
        self.cursor.execute("SELECT * FROM ordens_servico")
        ordens = self.cursor.fetchall()

        for ordem in ordens:
            ordem_text = f"ID: {ordem[0]} | Cliente: {ordem[1]} | Descrição: {ordem[2]} | Data: {ordem[3]}"
            listbox.insert(tk.END, ordem_text)

        # Associa o clique direito à exibição do menu
        listbox.bind("<Button-3>", show_context_menu)

    def edit_ordem(self, listbox):
        if hasattr(self, 'selected_ordem'):
            ordem_text = listbox.get(self.selected_ordem)
            ordem_id = ordem_text.split(" | ")[0].split(": ")[1]

            self.cursor.execute("SELECT * FROM ordens_servico WHERE id = ?", (ordem_id,))
            ordem = self.cursor.fetchone()

            edit_window = tk.Toplevel(self.root)
            edit_window.title("Editar Ordem de Serviço")
            edit_window.geometry("400x300")
            edit_window.config(bg="#f7f7f7")

            nome_cliente_label = tk.Label(edit_window, text="Nome do Cliente", bg="#f7f7f7", font=("Helvetica", 12))
            nome_cliente_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
            nome_cliente_entry = tk.Entry(edit_window, font=("Helvetica", 12), width=30)
            nome_cliente_entry.insert(0, ordem[1])
            nome_cliente_entry.grid(row=0, column=1, padx=10, pady=10)

            descricao_label = tk.Label(edit_window, text="Descrição do Serviço", bg="#f7f7f7", font=("Helvetica", 12))
            descricao_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
            descricao_entry = tk.Entry(edit_window, font=("Helvetica", 12), width=30)
            descricao_entry.insert(0, ordem[2])
            descricao_entry.grid(row=1, column=1, padx=10, pady=10)

            data_label = tk.Label(edit_window, text="Data da Ordem", bg="#f7f7f7", font=("Helvetica", 12))
            data_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
            data_entry = tk.Entry(edit_window, font=("Helvetica", 12), width=30)
            data_entry.insert(0, ordem[3])
            data_entry.grid(row=2, column=1, padx=10, pady=10)

            save_button = tk.Button(edit_window, text="Salvar Alterações", command=lambda: self.save_edit(ordem_id, nome_cliente_entry.get(), descricao_entry.get(), data_entry.get(), edit_window), font=("Helvetica", 12), bg="#4CAF50", fg="white", relief="flat")
            save_button.grid(row=3, column=0, columnspan=2, pady=20)

    def save_edit(self, ordem_id, nome_cliente, descricao, data, edit_window):
        if nome_cliente and descricao and data:
            self.cursor.execute("""
                UPDATE ordens_servico
                SET nome_cliente = ?, descricao = ?, data = ?
                WHERE id = ?
            """, (nome_cliente, descricao, data, ordem_id))
            self.conn.commit()
            messagebox.showinfo("Sucesso", "Ordem de serviço editada com sucesso!")
            edit_window.destroy()
            self.view_ordens()
        else:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios.")

    def delete_ordem(self, listbox):
        if hasattr(self, 'selected_ordem'):
            ordem_text = listbox.get(self.selected_ordem)
            ordem_id = ordem_text.split(" | ")[0].split(": ")[1]

            self.cursor.execute("DELETE FROM ordens_servico WHERE id = ?", (ordem_id,))
            self.conn.commit()
            messagebox.showinfo("Sucesso", "Ordem de serviço excluída com sucesso!")
            self.view_ordens()

    def clear_entries(self):
        self.nome_cliente_entry.delete(0, tk.END)
        self.descricao_entry.delete(0, tk.END)
        self.data_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = OrdemServicoApp(root)
    root.mainloop()
