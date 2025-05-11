function showTaskMenu(button, event) {
  event.preventDefault();

  // Закрываем предыдущее меню
  if (activeContextMenu) {
    activeContextMenu.remove();
    activeContextMenu = null;
  }

  // Создаём меню с контейнером для стрелочки
  const menu = document.createElement("div");
  menu.className = "custom-context-menu";
  menu.innerHTML = `
    <div class="menu-pointer"></div>
    <div class="menu-vertical">
      <a href="${button.dataset.deleteUrl}" class="menu-link">🗑️ Delete</a>
    </div>
  `;

  document.body.appendChild(menu);
  activeContextMenu = menu;

  // Позиционируем меню и стрелочку
  positionMenuAtCursor(menu, event);

  // Закрытие при клике вне меню
  const closeMenu = (e) => {
    if (!menu.contains(e.target) && e.target !== button) {
      menu.remove();
      document.removeEventListener("click", closeMenu);
      activeContextMenu = null;
    }
  };
  document.addEventListener("click", closeMenu);
}

function positionMenuAtCursor(menu, event) {
  const { clientX: cursorX, clientY: cursorY } = event;

  // Добавляем меню в DOM
  if (!document.body.contains(menu)) {
    document.body.appendChild(menu);
  }

  // Временные стили для расчёта размеров
  menu.style.visibility = "hidden";
  menu.style.position = "fixed";
  menu.style.left = "0";
  menu.style.top = "0";

  // Получаем размеры
  const menuRect = menu.getBoundingClientRect();
  const pointerWidth = 12; // Ширина стрелочки
  const edgeMargin = 20;   // Минимальный отступ от краёв

  // Рассчитываем позицию меню
  let left = Math.max(5, Math.min(
    cursorX - menuRect.width / 2, // Центрируем относительно курсора
    window.innerWidth - menuRect.width - 5
  ));

  let top = cursorY + 10;
  let pointerDirection = "top";

  // Если не помещается снизу — показываем сверху
  if (top + menuRect.height > window.innerHeight) {
    top = cursorY - menuRect.height - 10;
    pointerDirection = "bottom";
  }

  // Финальная позиция меню
  menu.style.left = `${left}px`;
  menu.style.top = `${top}px`;
  menu.style.visibility = "visible";
  menu.style.zIndex = "10000";

  // Позиционируем стрелочку
  const pointer = menu.querySelector('.menu-pointer');
  if (pointer) {
    // Идеальная позиция (центр под курсором)
    let pointerOffset = cursorX - left - (pointerWidth / 2);

    // Корректируем у границ
    pointerOffset = Math.max(
      edgeMargin - (pointerWidth / 2), // Минимум с учётом ширины стрелки
      Math.min(
        pointerOffset,
        menuRect.width - edgeMargin - (pointerWidth / 2) // Максимум
      )
    );

    pointer.style.left = `${pointerOffset}px`;
    pointer.className = `menu-pointer pointer-${pointerDirection}`;
  }
}

// Закрываем все меню при клике вне их
document.addEventListener("click", (e) => {
  if (!e.target.closest(".custom-context-menu, .task-action-btn")) {
    document.querySelectorAll(".custom-context-menu").forEach(menu => menu.remove());
  }
});